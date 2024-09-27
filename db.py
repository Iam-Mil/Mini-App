import asyncpg
import logging

logger = logging.getLogger(__name__)


async def insert(user_id, username, email):
    conn = None
    try:
        conn = await asyncpg.connect(
            user='postgres',
            password='13243511',
            database='postgres',
            host='localhost',
            port=5432,
        )

        query = """
        INSERT INTO telegram_users(id, username, record, email)
        VALUES ($1, $2, 0, $3)
        ON CONFLICT (id) DO NOTHING;
        """  # Используйте ON CONFLICT для предотвращения ошибок при вставке дубликатов

        await conn.execute(query, user_id, username, email)
    except Exception as e:
        logger.error(f"Ошибка при вставке данных: {e}")
    finally:
        if conn:
            await conn.close()

