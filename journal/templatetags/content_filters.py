import re
from django import template
from django.utils.safestring import mark_safe
import markdown as md

register = template.Library()

YOUTUBE_EMBED_RE = re.compile(
    r"https?://(?:www\.)?youtube\.com/embed/[^\s]+"
)

@register.filter
def markdownify(text):
    return mark_safe(
        md.markdown(
            text,
            extensions=[
                "extra",
                "pymdownx.magiclink",  # auto-links bare URLs
            ],
            extension_configs={
                "pymdownx.magiclink": {
                    "repo_url_shortener": True,
                    "social_url_shortener": True,
                }
            }
        )
    )


@register.filter
def embed_youtube(text):
    def replace(match):
        url = match.group(0)  # full URL, unchanged
        return f"""<div class="iframe-container">
            <iframe
                src="{url}"
                title="YouTube video player"
                frameborder="0"
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
                referrerpolicy="strict-origin-when-cross-origin"
                allowfullscreen>
            </iframe>
        </div>
        """
    return mark_safe(YOUTUBE_EMBED_RE.sub(replace, text))