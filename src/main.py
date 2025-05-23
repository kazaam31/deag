"""Entry point for the ordering system."""

def add(a: int, b: int) -> int:
    """Return the sum of ``a`` and ``b``."""
    return a + b


def main() -> None:
    """Run a small demonstration of the ordering system."""
    result = add(2, 2)
    print(f"2 + 2 = {result}")

if __name__ == "__main__":
    main()
