from typing import List, Dict, Any
from collections import namedtuple
import psycopg2
from psycopg2 import extras
from dotenv import load_dotenv
import os


load_dotenv()


DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

Problem = namedtuple("Problem", ["id", "status", "name"])
Category = namedtuple("Category", ["id", "name", "description"])
Variant = namedtuple("Variant", ["id", "type", "order", "content", "is_preferred"])
Rating = namedtuple(
    "Rating", ["problem_variant_id", "user_id", "rating_type", "rating_rating"]
)
SubProblem = namedtuple("SubProblem", ["id", "order", "content"])


class Database:
    def __init__(self):
        self.conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
        )

    def fetch_data(self, user_id: str) -> List[Dict[str, Any]]:
        data = []

        try:
            with self.conn.cursor(cursor_factory=extras.NamedTupleCursor) as cur:
                cur.execute(
                    "SELECT id, name, status FROM problems WHERE created_by = %s",
                    (user_id,),
                )
                problems = [Problem(*row) for row in cur.fetchall()]

                for problem in problems:
                    # Fetch category_id from the link table
                    cur.execute(
                        "SELECT problem_category_id FROM problem_category_links WHERE problem_id = %s",
                        (problem.id,),
                    )
                    category_id = cur.fetchone()[0]

                    # Fetch the category based on category_id
                    cur.execute(
                        "SELECT id, name, description FROM problem_categories WHERE id = %s",
                        (category_id,),
                    )
                    category = Category(*cur.fetchone())

                    # Fetch variants
                    cur.execute(
                        'SELECT id, type, "order", content, is_preferred FROM problem_variants WHERE problem_id = %s',
                        (problem.id,),
                    )
                    variants = [Variant(*row) for row in cur.fetchall()]
                    variant_list = []

                    for variant in variants:
                        cur.execute(
                            "SELECT problem_variant_id, user_id, rating_type, rating FROM problem_variant_ratings WHERE problem_variant_id = %s",
                            (variant.id,),
                        )
                        ratings = [Rating(*row) for row in cur.fetchall()]

                        cur.execute(
                            'SELECT problem_variant_id, "order", content FROM sub_problems WHERE problem_variant_id = %s',
                            (variant.id,),
                        )
                        sub_problems = [SubProblem(*row) for row in cur.fetchall()]

                        variant_list.append(
                            {
                                "type": variant.type,
                                "order": variant.order,
                                "content": variant.content,
                                "is_preferred": variant.is_preferred,
                                "ratings": [r._asdict() for r in ratings],
                                "sub_problems": [sp.content for sp in sub_problems],
                            }
                        )

                    data.append(
                        {
                            "status": problem.status,
                            "name": problem.name,
                            "category": category._asdict(),
                            "variants": variant_list,
                        }
                    )
        except Exception as e:
            print(f"An error occurred: {e}")

        return data

    def fetch_username(self, user_id: str) -> str:
        try:
            with self.conn.cursor() as cur:
                cur.execute("SELECT first_name FROM users WHERE id = %s", (user_id,))
                result = cur.fetchone()
                if result:
                    return result[0]
        except Exception as e:
            print(f"An error occurred while fetching the username: {e}")
