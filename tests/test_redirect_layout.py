from pathlib import Path


def test_redirect_layout_uses_page_redirect_target():
    layout = Path("_layouts/default.html").read_text(encoding="utf-8")

    assert "{%- elsif page.redirect contains '://' -%}" in layout
    assert 'content="0; url={{ page.redirect }}"' in layout


def test_redirect_layout_keeps_404_boolean_redirect_behavior():
    layout = Path("_layouts/default.html").read_text(encoding="utf-8")

    assert "{%- if page.redirect == true -%}" in layout
    assert 'content="3; url={{ site.baseurl }}/"' in layout
