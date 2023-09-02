from datetime import datetime
import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

conn = psycopg2.connect(
    host=DB_HOST,
    port=DB_PORT,
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
)
cur = conn.cursor()

sample_data = [
    {
        "status": "Open",
        "name": "How can we improve user engagement?",
        "category": {
            "name": "User Experience",
            "description": "Related to user interaction",
        },
        "variants": [
            {
                "type": "ROOT",
                "order": 0,
                "content": "How can we make our homepage more engaging?",
                "is_preferred": True,
                "ratings": [
                    {"type": "passion", "rating": 5},
                    {"type": "importance", "rating": 4},
                ],
                "sub_problems": [
                    "How to improve homepage layout?",
                    "How to make homepage load faster?",
                ],
            },
            {
                "type": "STEP_UP",
                "order": 1,
                "content": "How can we gamify user engagement?",
                "is_preferred": False,
                "ratings": [{"type": "passion", "rating": 3}],
                "sub_problems": ["Which elements to gamify?", "What rewards to give?"],
            },
        ],
    },
    {
        "status": "In Progress",
        "name": "How to reduce the time needed to go from idea to prototype?",
        "category": {
            "name": "Product Development",
            "description": "Related to creating new products",
        },
        "variants": [
            {
                "type": "ROOT",
                "order": 0,
                "content": "How to streamline the prototyping process?",
                "is_preferred": True,
                "ratings": [
                    {"type": "passion", "rating": 4},
                    {"type": "importance", "rating": 5},
                ],
                "sub_problems": [
                    "How to automate the prototyping?",
                    "How to quickly gather requirements?",
                ],
            }
        ],
    },
    {
        "status": "Open",
        "name": "How can we improve the onboarding process?",
        "category": {
            "name": "User Experience",
            "description": "Related to user interaction",
        },
        "variants": [
            {
                "type": "ROOT",
                "order": 0,
                "content": "How can we make the onboarding more intuitive?",
                "is_preferred": True,
                "ratings": [
                    {"type": "passion", "rating": 4},
                    {"type": "importance", "rating": 3},
                ],
                "sub_problems": [
                    "How to simplify sign-up?",
                    "How to provide initial guidance?",
                ],
            },
            {
                "type": "STEP_DOWN",
                "order": -1,
                "content": "How to reduce the number of steps in the onboarding process?",
                "is_preferred": False,
                "ratings": [{"type": "importance", "rating": 5}],
                "sub_problems": [
                    "Which steps can be eliminated?",
                    "How to compress multiple steps?",
                ],
            },
        ],
    },
    {
        "status": "Closed",
        "name": "How to increase user retention?",
        "category": {
            "name": "User Growth",
            "description": "Related to retaining users",
        },
        "variants": [
            {
                "type": "ROOT",
                "order": 0,
                "content": "What features make users stick around?",
                "is_preferred": True,
                "ratings": [
                    {"type": "passion", "rating": 5},
                    {"type": "favorite", "rating": 5},
                ],
                "sub_problems": [
                    "What rewards can we offer?",
                    "How to improve user engagement?",
                ],
            },
            {
                "type": "STEP_UP",
                "order": 1,
                "content": "How can we improve the long-term user experience?",
                "is_preferred": False,
                "ratings": [{"type": "importance", "rating": 4}],
                "sub_problems": [
                    "How to add value over time?",
                    "How to gather long-term feedback?",
                ],
            },
        ],
    },
    {
        "status": "In Progress",
        "name": "How can we reduce customer service wait times?",
        "category": {
            "name": "Customer Service",
            "description": "Related to customer support",
        },
        "variants": [
            {
                "type": "ROOT",
                "order": 0,
                "content": "How can we automate customer support?",
                "is_preferred": True,
                "ratings": [
                    {"type": "passion", "rating": 4},
                    {"type": "importance", "rating": 5},
                ],
                "sub_problems": ["Chatbot design?", "AI response accuracy?"],
            },
            {
                "type": "STEP_DOWN",
                "order": -1,
                "content": "How can we optimize the current manual support?",
                "is_preferred": False,
                "ratings": [{"type": "passion", "rating": 3}],
                "sub_problems": ["Training?", "Faster response techniques?"],
            },
        ],
    },
    {
        "status": "Open",
        "name": "How to improve code quality?",
        "category": {
            "name": "Software Development",
            "description": "Related to code quality and maintainability",
        },
        "variants": [
            {
                "type": "ROOT",
                "order": 0,
                "content": "How can we include automated testing in our CI/CD pipeline?",
                "is_preferred": True,
                "ratings": [
                    {"type": "passion", "rating": 5},
                    {"type": "favorite", "rating": 4},
                ],
                "sub_problems": ["Choice of testing frameworks?", "Code coverage?"],
            },
            {
                "type": "STEP_UP",
                "order": 1,
                "content": "How can we improve the overall software architecture?",
                "is_preferred": False,
                "ratings": [{"type": "importance", "rating": 4}],
                "sub_problems": ["Microservices?", "API design?"],
            },
        ],
    },
    {
        "status": "Closed",
        "name": "How to improve data security?",
        "category": {
            "name": "Data Management",
            "description": "Related to data storage and protection",
        },
        "variants": [
            {
                "type": "ROOT",
                "order": 0,
                "content": "How can we improve encryption methods?",
                "is_preferred": True,
                "ratings": [
                    {"type": "passion", "rating": 5},
                    {"type": "favorite", "rating": 5},
                ],
                "sub_problems": ["Symmetric vs Asymmetric?", "Hardware encryption?"],
            },
            {
                "type": "STEP_DOWN",
                "order": -1,
                "content": "How can we improve user authentication?",
                "is_preferred": False,
                "ratings": [{"type": "importance", "rating": 5}],
                "sub_problems": ["Two-factor authentication?", "Biometrics?"],
            },
        ],
    },
    {
        "status": "Open",
        "name": "How can we improve team collaboration?",
        "category": {
            "name": "Team Management",
            "description": "Related to team dynamics and performance",
        },
        "variants": [
            {
                "type": "ROOT",
                "order": 0,
                "content": "How can we improve communication among team members?",
                "is_preferred": True,
                "ratings": [
                    {"type": "passion", "rating": 5},
                    {"type": "importance", "rating": 4},
                ],
                "sub_problems": [
                    "How to choose the right communication tools?",
                    "How to establish an effective meeting schedule?",
                ],
            },
            {
                "type": "STEP_UP",
                "order": 1,
                "content": "How can we foster a culture of continuous improvement?",
                "is_preferred": False,
                "ratings": [{"type": "passion", "rating": 3}],
                "sub_problems": [
                    "What KPIs should we track?",
                    "How to give and receive constructive feedback?",
                ],
            },
            {
                "type": "STEP_UP",
                "order": 2,
                "content": "How to facilitate cross-functional collaboration?",
                "is_preferred": False,
                "ratings": [{"type": "importance", "rating": 4}],
                "sub_problems": [
                    "How to choose representatives for cross-functional teams?",
                    "How to align team goals?",
                ],
            },
            {
                "type": "STEP_DOWN",
                "order": -1,
                "content": "How to make remote team members feel included?",
                "is_preferred": False,
                "ratings": [{"type": "importance", "rating": 5}],
                "sub_problems": [
                    "What kind of virtual team-building activities can we do?",
                    "How to adjust communication channels for remote work?",
                ],
            },
            {
                "type": "STEP_DOWN",
                "order": -2,
                "content": "How to deal with conflicts within the team?",
                "is_preferred": False,
                "ratings": [{"type": "favorite", "rating": 4}],
                "sub_problems": [
                    "What is the best conflict resolution strategy?",
                    "How to preempt conflicts?",
                ],
            },
            {
                "type": "STEP_DOWN",
                "order": -3,
                "content": "How to train new team members efficiently?",
                "is_preferred": False,
                "ratings": [{"type": "importance", "rating": 3}],
                "sub_problems": [
                    "What should the onboarding process look like?",
                    "How to mentor new hires?",
                ],
            },
        ],
    },
    {
        "status": "In Progress",
        "name": "How to enhance mobile app performance?",
        "category": {
            "name": "Software Development",
            "description": "Related to mobile application development and performance",
        },
        "variants": [
            {
                "type": "ROOT",
                "order": 0,
                "content": "How can we reduce app crashes?",
                "is_preferred": True,
                "ratings": [
                    {"type": "passion", "rating": 4},
                    {"type": "importance", "rating": 5},
                ],
                "sub_problems": [
                    "How to set up effective crash analytics?",
                    "How to prioritize and fix bugs?",
                ],
            },
            {
                "type": "STEP_UP",
                "order": 1,
                "content": "How to improve app load times?",
                "is_preferred": False,
                "ratings": [{"type": "favorite", "rating": 4}],
                "sub_problems": ["How to optimize assets?", "How to use lazy loading?"],
            },
            {
                "type": "STEP_UP",
                "order": 2,
                "content": "How to ensure seamless user experience across different devices?",
                "is_preferred": False,
                "ratings": [{"type": "importance", "rating": 5}],
                "sub_problems": [
                    "How to perform device-specific testing?",
                    "How to adapt UI/UX for various screen sizes?",
                ],
            },
            {
                "type": "STEP_DOWN",
                "order": -1,
                "content": "How to quickly roll out hotfixes?",
                "is_preferred": False,
                "ratings": [{"type": "passion", "rating": 3}],
                "sub_problems": [
                    "How to set up automated deployment?",
                    "How to notify users about updates?",
                ],
            },
            {
                "type": "STEP_DOWN",
                "order": -2,
                "content": "How to collect user feedback on app performance?",
                "is_preferred": False,
                "ratings": [{"type": "importance", "rating": 3}],
                "sub_problems": [
                    "How to design user surveys?",
                    "How to collect crash reports?",
                ],
            },
            {
                "type": "STEP_DOWN",
                "order": -3,
                "content": "How to allocate resources for app maintenance?",
                "is_preferred": False,
                "ratings": [{"type": "favorite", "rating": 2}],
                "sub_problems": [
                    "How to estimate maintenance costs?",
                    "How to allocate developer time for maintenance vs new features?",
                ],
            },
        ],
    },
    {
        "status": "Open",
        "name": "How to increase customer retention?",
        "category": {
            "name": "Customer Success",
            "description": "Related to retaining and delighting existing customers",
        },
        "variants": [
            {
                "type": "ROOT",
                "order": 0,
                "content": "How can we improve customer support?",
                "is_preferred": True,
                "ratings": [
                    {"type": "passion", "rating": 4},
                    {"type": "importance", "rating": 5},
                ],
                "sub_problems": [
                    "How to optimize support ticket resolution?",
                    "How to train customer support agents?",
                ],
            },
            {
                "type": "STEP_UP",
                "order": 1,
                "content": "How can we enhance the customer journey?",
                "is_preferred": False,
                "ratings": [{"type": "favorite", "rating": 5}],
                "sub_problems": [
                    "How to map the customer journey?",
                    "How to identify touchpoints for improvement?",
                ],
            },
            {
                "type": "STEP_UP",
                "order": 2,
                "content": "How to implement an effective loyalty program?",
                "is_preferred": False,
                "ratings": [{"type": "importance", "rating": 4}],
                "sub_problems": [
                    "How to identify rewards that resonate with customers?",
                    "How to track loyalty program effectiveness?",
                ],
            },
            {
                "type": "STEP_DOWN",
                "order": -1,
                "content": "How to reduce churn rate?",
                "is_preferred": False,
                "ratings": [{"type": "passion", "rating": 3}],
                "sub_problems": [
                    "How to identify at-risk customers?",
                    "How to design churn prevention strategies?",
                ],
            },
            {
                "type": "STEP_DOWN",
                "order": -2,
                "content": "How to collect customer feedback effectively?",
                "is_preferred": False,
                "ratings": [{"type": "favorite", "rating": 4}],
                "sub_problems": [
                    "How to design customer surveys?",
                    "How to collect qualitative feedback?",
                ],
            },
            {
                "type": "STEP_DOWN",
                "order": -3,
                "content": "How to handle customer complaints?",
                "is_preferred": False,
                "ratings": [{"type": "importance", "rating": 3}],
                "sub_problems": [
                    "How to log and categorize complaints?",
                    "How to conduct a root cause analysis?",
                ],
            },
        ],
    },
    {
        "status": "In Progress",
        "name": "How to increase website traffic?",
        "category": {
            "name": "Marketing",
            "description": "Related to increasing and optimizing website traffic",
        },
        "variants": [
            {
                "type": "ROOT",
                "order": 0,
                "content": "How to improve SEO?",
                "is_preferred": True,
                "ratings": [
                    {"type": "passion", "rating": 5},
                    {"type": "importance", "rating": 4},
                ],
                "sub_problems": [
                    "How to conduct keyword research?",
                    "How to optimize on-page SEO?",
                ],
            },
            {
                "type": "STEP_UP",
                "order": 1,
                "content": "How to optimize content marketing?",
                "is_preferred": False,
                "ratings": [{"type": "favorite", "rating": 5}],
                "sub_problems": [
                    "How to develop a content calendar?",
                    "How to measure content performance?",
                ],
            },
            {
                "type": "STEP_UP",
                "order": 2,
                "content": "How to increase social media engagement?",
                "is_preferred": False,
                "ratings": [{"type": "importance", "rating": 3}],
                "sub_problems": [
                    "How to choose the right social media platforms?",
                    "How to design engaging posts?",
                ],
            },
            {
                "type": "STEP_DOWN",
                "order": -1,
                "content": "How to implement effective PPC campaigns?",
                "is_preferred": False,
                "ratings": [{"type": "passion", "rating": 2}],
                "sub_problems": [
                    "How to choose PPC keywords?",
                    "How to set campaign budgets?",
                ],
            },
            {
                "type": "STEP_DOWN",
                "order": -2,
                "content": "How to improve website UX for better conversions?",
                "is_preferred": False,
                "ratings": [{"type": "importance", "rating": 4}],
                "sub_problems": [
                    "How to conduct A/B tests?",
                    "How to analyze user behavior?",
                ],
            },
            {
                "type": "STEP_DOWN",
                "order": -3,
                "content": "How to optimize email marketing?",
                "is_preferred": False,
                "ratings": [{"type": "favorite", "rating": 3}],
                "sub_problems": [
                    "How to build an email list?",
                    "How to design effective email templates?",
                ],
            },
        ],
    },
]


def populate_db(user_id, data):
    for problem in data:
        # Add problem
        current_time = datetime.utcnow()
        cur.execute(
            "INSERT INTO problems (created_by, status, name, created_at) VALUES (%s, %s, %s, %s) RETURNING id;",
            (user_id, problem["status"], problem["name"], current_time),
        )
        problem_id = cur.fetchone()[0]

        # Add category
        category = problem.get("category", {})
        cur.execute(
            "INSERT INTO problem_categories (name, description, created_by, created_at) VALUES (%s, %s, %s, %s) RETURNING id;",
            (category["name"], category["description"], user_id, current_time),
        )
        category_id = cur.fetchone()[0]

        # Link problem and category
        cur.execute(
            "INSERT INTO problem_category_links (problem_category_id, problem_id, created_by, created_at) VALUES (%s, %s, %s, %s);",
            (category_id, problem_id, user_id, current_time),
        )

        # Add variants, ratings, and subproblems
        for variant in problem["variants"]:
            cur.execute(
                'INSERT INTO problem_variants (problem_id, type, created_by, "order", content, is_preferred, created_at) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING id;',
                (
                    problem_id,
                    variant["type"],
                    user_id,
                    variant["order"],
                    variant["content"],
                    variant["is_preferred"],
                    current_time,
                ),
            )
            variant_id = cur.fetchone()[0]

            # Add ratings
            for rating in variant["ratings"]:
                cur.execute(
                    "INSERT INTO problem_variant_ratings (problem_variant_id, user_id, rating_type, rating, created_at) VALUES (%s, %s, %s, %s, %s);",
                    (
                        variant_id,
                        user_id,
                        rating["type"],
                        rating["rating"],
                        current_time,
                    ),
                )

            # Add subproblems
            for sub_problem_order, sub_problem_content in enumerate(
                variant["sub_problems"]
            ):
                cur.execute(
                    'INSERT INTO sub_problems (problem_variant_id, created_by, "order", content, created_at) VALUES (%s, %s, %s, %s, %s);',
                    (
                        variant_id,
                        user_id,
                        sub_problem_order,
                        sub_problem_content,
                        current_time,
                    ),
                )

    conn.commit()


def delete_all_data_except_users():
    tables_to_clear = [
        "problem_category_links",
        "sub_problems",
        "problem_variant_ratings",
        "problem_variants",
        "problems",
        "problem_categories",
    ]

    for table in tables_to_clear:
        cur.execute(f"DELETE FROM {table} WHERE 1=1;")

    conn.commit()


delete_all_data_except_users()

populate_db(os.getenv("USER_ID"), sample_data)

cur.close()
conn.close()
