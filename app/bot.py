from pathlib import Path
from typing import Tuple

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from botspot.core.bot_manager import BotManager
from calmlib.utils import setup_logger
from dotenv import load_dotenv
from loguru import logger

# Load environment variables
load_dotenv(Path(__file__).parent.parent / ".env")

from .router import app
from .router import router as main_router

# from router import app, router
from .routers.settings import router as settings_router

# Initialize bot and dispatcher
dp = Dispatcher()
dp.include_router(main_router)
dp.include_router(settings_router)


def main(debug=False) -> Tuple[BotManager, Bot]:
    setup_logger(logger, level="DEBUG" if debug else "INFO")

    # Initialize Bot instance with a default parse mode
    bot = Bot(
        token=app.config.telegram_bot_token, default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )

    # Initialize BotManager with default components
    bm = BotManager(
        bot=bot,
        # error_handler={"enabled": True},
        # ask_user={"enabled": True},
        # bot_commands_menu={"enabled": True},
    )

    # Setup dispatcher with our components
    bm.setup_dispatcher(dp)

    # Start polling
    dp.run_polling(bot)

    return bm, bot


if __name__ == "__main__":
    main()
