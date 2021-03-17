from django.db import models
from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib import messages
from modelcluster.fields import ParentalKey

from wagtail.core import blocks
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page, Orderable
from wagtail.embeds.blocks import EmbedBlock
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, InlinePanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtailvideos.blocks import VideoChooserBlock
from wagtail.documents.blocks import DocumentChooserBlock


from tinymce.models import HTMLField



class HomePage(Page):
    section_title = models.CharField(max_length=60)
    text = models.TextField()

    content_panels = Page.content_panels + [
        FieldPanel('section_title'),
        FieldPanel('text')
    ]
    
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["courses"] = CoursePage.objects.all()
        context["active_page"] = "home"
        return context


class AboutPage(Page):
    content = RichTextField()

    content_panels = Page.content_panels + [
        FieldPanel('content')
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["active_page"] = "about"
        return context

class CoursePage(Page):
    description = RichTextField()
    cover_image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.SET_NULL, null=True, related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('description'),
        ImageChooserPanel('cover_image'),
    ]


class ActivityPage(Page):
    body = RichTextField()
    cover_image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.SET_NULL, null=True, related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('body'),
        ImageChooserPanel('cover_image'),
        InlinePanel('resources'),
    ]

    def serve(self, request, *args, **kwargs):
        from .forms import PostForm
        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.page = self
                if request.user.is_authenticated:
                    post.user = request.user
                post.save()
                messages.success(request, "Sucesso!")
                form = PostForm()
        else:
            form = PostForm()

        return render(request, self.template, {"page": self, "form": form})


class Resource(Orderable):
    page = ParentalKey(ActivityPage, on_delete=models.CASCADE, related_name="resources")
    content = StreamField([
        ("heading", blocks.CharBlock()),
        ("paragraph", blocks.RichTextBlock()),
        ("embed", EmbedBlock()),
        ("image", ImageChooserBlock()),
        ("video", VideoChooserBlock()),
        ("document", DocumentChooserBlock()),
    ])

    panels = [
        StreamFieldPanel('content'),
    ]


class Post(models.Model):
    page = ParentalKey(ActivityPage, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)
    text = HTMLField()
    response_to = models.ForeignKey('self', on_delete=models.CASCADE, related_name="responses", null=True)
