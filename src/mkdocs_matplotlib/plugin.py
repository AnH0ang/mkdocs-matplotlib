import base64
import tempfile
from textwrap import dedent
from typing import Any, Dict

from bs4 import BeautifulSoup
from mkdocs.config.base import Config
from mkdocs.plugins import BasePlugin
from mkdocs.structure.files import Files
from mkdocs.structure.pages import Page

RENDER_SWITCH = "# mkdocs: render"


def _rendered_image_to_dir(save_img_dir: str, render_code: str) -> None:
    # snippet to save a figure
    clearplot_code = """
    import matplotlib.pyplot as plt
    plt.figure()
    """
    clearplot_code = dedent(clearplot_code)

    savefig_code = f"""
    plt.savefig("{save_img_dir}")
    plt.close()
    """
    savefig_code = dedent(savefig_code)

    # render image to
    global_namespace: Dict[str, Any] = {}
    local_namespace: Dict[str, Any] = {}
    exec(clearplot_code, global_namespace, local_namespace)
    exec(render_code, global_namespace, local_namespace)
    exec(savefig_code, global_namespace, local_namespace)


class RenderPlugin(BasePlugin):
    """An `mkdocs` plugin.
    This plugin defines the following event hooks:
    - `on_page_content`
    Check the [Developing Plugins](https://www.mkdocs.org/user-guide/plugins/#developing-plugins) page of `mkdocs`
    for more information about its plugin system.
    """

    def on_page_content(
        self, html: str, page: Page, config: Config, files: Files
    ) -> str:
        """Renders the code cells with matplotlib.

        Search for code cells in the passed HTML string. If there is a code cell and it starts
        with the correct comment, execute it and paste the rendered image in an img tag.

        Args:
            html: Input Html
            page: Page Info
            config: Mkdocs Config
            files: File Info

        Returns:
            Html with rendered images added.
        """
        soup = BeautifulSoup(html, features="html.parser")
        for code_tag in soup.find_all("code"):
            temp_file = tempfile.NamedTemporaryFile(suffix=".png").name

            # skip if not a multi line code cell
            if code_tag.parent.name != "pre":
                continue

            # only render if cell start with correct comment
            if code_tag.text.startswith(RENDER_SWITCH):
                _rendered_image_to_dir(temp_file, code_tag.text)

                # insert image tag
                with open(temp_file, "rb") as f:
                    encoded = base64.b64encode(f.read()).decode("ascii")
                    img_tag = soup.new_tag(
                        "img", src="data:image/png;base64,{}".format(encoded)
                    )
                    code_tag.parent.insert_after(img_tag)
                    img_tag.wrap(soup.new_tag("center"))

        return str(soup)
