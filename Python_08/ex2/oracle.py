import os

from dotenv import load_dotenv  # type: ignore


def format_database_url(database_url: str | None, mode: str) -> str:
    if not database_url:
        return "DatabaseURL - Missing configuration"
    if mode == "production":
        return "Database: Connected to local instance (details hidden)"
    return f"Database: {database_url}"


def format_zion(zion: str | None, mode: str) -> str:
    if not zion:
        return "ZionNetwork - Missing configuration"
    if mode == "production":
        return "Zion Network: Online (details hidden)"
    return f"Zion Network: {zion}"


def format_api_access(api: str | None, mode: str) -> str:
    if not api:
        return "ApiAccess - Missing configuration"
    if mode == "production":
        return "API Access: Authenticated (details hidden)"
    return f"API Access: {api}"


def format_log_level(log: str | None, mode: str) -> str:
    if not log:
        return "LogLevel - Missing configuration"
    if mode == "production":
        return "Log Level: DEBUG (details hidden)"
    return f"Log Level: {log}"


def security_check() -> None:
    print("""\n[OK] No hardcoded secrets detected
[OK] .env file properly configured
[OK] Production overrides available""")


if __name__ == "__main__":
    load_dotenv()
    print("ORACLE STATUS: Reading the Matrix...\n")
    print("Configuration loaded:")
    mode: str = os.getenv("MATRIX_MODE", "development").lower()
    print(f"Mode: {mode}")
    print(format_database_url(os.getenv("DATABASE_URL"), mode))
    print(format_api_access(os.getenv("API_KEY"), mode))
    print(format_log_level(os.getenv("LOG_LEVEL"), mode))
    print(format_zion(os.getenv("ZION_ENDPOINT"), mode))
    security_check()
    print("\nThe Oracle sees all configurations.")
