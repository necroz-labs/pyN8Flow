import json
from pathlib import Path


class Workflow:
    """
    Represents a workflow that can be saved as a JSON file.
    """
    def __init__(self, name: str):
        self.name = name
        self.content = None

    def save(self, path: str | Path, *, overwrite: bool = False) -> None:
        """
        Save the workflow content to a JSON file.

        Args:
            path (str | Path): The file path where the workflow will be saved.
            overwrite (bool, optional): Whether to overwrite an existing file. Defaults to False.

        Raises:
            ValueError: If the file already exists and overwrite=False.
            ValueError: If the workflow content is None.
        """
        if self.content is None:
            raise ValueError(
                "An empty workflow does not make much sense. "
                "Wouldn't it make more sense to add something to the workflow?"
            )

        file_path = Path(path) if isinstance(path, str) else path

        if file_path.is_file() and not overwrite:
            msg = "A file with the same name already exists"
            raise ValueError(msg)

        with file_path.open("w", encoding="utf-8") as f:
            json.dump(self.content, f, ensure_ascii=False, indent=4)
