from typer.testing import CliRunner

from minilake.cli import main

runner = CliRunner()  # usuario do terminal ( simulação )


def test_add_beer():
    result = runner.invoke(
        main, ["add", "Skol", "KornPA", "--flavor=1", "--image=1", "--cost=2"]
    )
    assert result.exit_code == 0
    assert "Beer added" in result.stdout
