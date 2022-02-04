# Notes

## Chapter 1

- Responsive designs are made possible with a flexible layout, fluid images, and media queries
- A `meta` tag is needed in the head of your HTML so a browser knows how to render the page
- You'll want all images to be set with a `max-width` of 100% in the CSS by default
- A breakpoint is just a point, typically a screen-width, at which we use a media query to alter the design
- When you write CSS for a responsive design, start with base styles that can work on any device—typically the smallest screen and then use media queries to adapt it for larger screens
- Presently the void tags are `area`, `base`, `br`, `col`, `embed`, `hr`, `img`, `input`, `link`, `meta`, `param`, `source`, `track`, and `wbr`.
- Consider the HTML5 Boilerplate (http://html5boilerplate.com/). It's a premade best practice HTML5 file. You can also custom build the template to match your specific needs.
- The `<section>`element is used to define a generic section of a document or application.
- The `<nav>` element is used to wrap major navigational links to other pages or parts within the same page. 
- The `<article>` element is used to wrap a self-contained piece of content. When structuring a page, ask whether the content you're intending to use within an `<article>` tag could be taken as a whole lump and pasted onto a different site and still make complete sense.
- The `<aside>` element is used for content that is tangentially related to the content around it. In practical terms, I often use it for sidebars, or content as a little tip about a related subject in a blog post.
- Practically, the `<header>` can be used for the "masthead" area of a site's header but also as an introduction to other content, such as an introduction section within an `<article>` element.
-  Like the `<header>`, it can be used multiple times within a page if needed. For example, it could be used for the footer of a blog but also a footer within a blog post `<article>`.
- However, the specification notes that contact information for the author of a blog post should instead be wrapped by an `<address>` element.
- h1–h6 elements must not be used to mark up subheadings, subtitles, alternative titles and taglines unless intended to be the heading for a new section or subsection.


## Chapter 3
- you can use any CSS length unit to specify media queries. Pixels (px) are the most commonly used but ems (em) and rems (rem) are equally valid and applicable.
- Therefore, unless you want to target styles to particular media types, just leave the screen and part out. That's the way we will be writing media queries in the example files from this point on. For example:
```css
@media (min-width: 750px) {
    /* styles */
}
```
- note that "render blocking" only refers to whether the browser will have to hold the initial rendering of the page on that resource. In either case, the CSS asset is still downloaded by the browser, albeit with a lower priority for non-blocking resources.
- The pointer media feature is used to query about the presence and accuracy of a pointing device such as a mouse.
