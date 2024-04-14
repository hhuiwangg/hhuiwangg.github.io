---
layout: page
title: MELP Level Set
img: assets/img/publication_preview/melp-levelset-preview.jpg
importance: 1
category: research
---

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.html path="assets/img/melp-levelset/representative.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

<br>

<div id="one" class="bal-container">
    <div class="bal-after">
        <img src="assets/img/melp-levelset/double_bubble.el.0400.jpg">
        <div class="bal-afterPosition afterLabel">
            After
        </div>
    </div>
    <div class="bal-before">
        <div class="bal-before-inset">
            <img src="assets/img/melp-levelset/double_bubble.render.0400.jpg">
            <div class="bal-beforePosition beforeLabel">
                Before
            </div>
        </div>
    </div>
    <div class="bal-handle">
        <span class=" handle-left-arrow"></span>
        <span class="handle-right-arrow"></span>
    </div>
</div>

<script src="js/script.js"></script>

<script>
    new BeforeAfter({
        id: '#one'
    });
    new BeforeAfter({
        id: '#two'
    });
    new BeforeAfter({
        id: '#three'
    });
</script>