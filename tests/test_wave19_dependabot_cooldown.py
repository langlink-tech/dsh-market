from pathlib import Path
def test_cooldown():
    dep = (Path(__file__).resolve().parents[1] / ".github" / "dependabot.yml").read_text()
    assert "package-ecosystem: github-actions" in dep
    assert "rebase-strategy: disabled" in dep
    assert "default-days: 10" in dep
