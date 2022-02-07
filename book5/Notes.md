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
- There are three possible states for the pointer features: none, coarse, and fine

## Chapter 4
- the formula to transform a fiexed element to a fluid is: target, divided by context, equals result.
- display: flex: This is the bread and butter of Flexbox. This merely sets the item to be a Flexbox, as opposed to a block or inline-block.
- align-items: This aligns the items within a Flexbox in the cross axis, vertically centering the text in our example.
- justify-content: This sets the main axis, centering the content. With a Flexbox row, you can think of it as the button in a word processor that sets the text to the left, right, or center
- When items are set as inline-flex anonymously, which happens if their parent element is not set to `display: flex`, then they retain whitespace between elements, just like inline-block or `inline-table` do. However, if they are within a flex container, then whitespace is removed, much as it is with CSS `table-cell` items within a CSS table.
- The align-items property positions items in the cross axis
- `flex-start`: Setting an element to `flex-start` would make it begin at the "starting" edge of its flex container.
- `flex-end`: Setting to `flex-end` would align the element at the end of the flex container.
- `center:` This puts it in the middle of the flex container.
- `baseline:` This sets all the flex items in the container so that their baselines align.
- `stretch:` This makes the items stretch to the size of their flex container (in the cross axis).
- `flex-grow` (the first value you can pass to flex) is the amount, in relation to the other flex items, the flex item can grow when free space is available.
- `flex-shrink `is the amount the flex item can shrink, in relation to the other flex items, when there is not enough space available.
- `flex-basis` (the final value you can pass to flex) is the basis size the flex item is sized to.
- The `order`property lets us revise the order of items within a Flexbox simply and sanely. In this example, a value of `-1` means that we want it to be before all the others.

## Chapter 5
- You need to use display grid to define a grid block
- If you don't want the grid block take all the space you need to use inline grid
- grid row auto flow and grid column auto flow is to add implicit rows and columns when there is free space

## Chapter 6
- The key thing to remember with pseudo-elements is that if you don't provide a value for content, nothing will show on the page
- CSS3 added the ability to select elements based upon the substring of their attribute selector.
- Likewise, if we wanted to select every third element, rather than write :nth-child(3n+3), we could just write :nth-child(3n) as every third item would begin at the third item anyway, without needing to state it explicitly.
- :nth-of-type and :nth-last-of-type let you be specific about the type of item you want to select.
- The ~ symbol, called "tilde," says "every subsequent sibling."
- The native solution to forking code in CSS is to use "feature queries," part of the CSS Conditional Rules Module Level 3 (http://www.w3.org/TR/css3-conditional/). Support was introduced in iOS and Safari 9, Firefox 22, Edge 12, and Chrome 28.
```css
@supports (flashing-sausages: lincolnshire) {
  body {
    sausage-sound: sizzling;
    sausage-color: slighty-burnt;
    background-color: brown;
  }
}
```
- If your main font is a web font, it's a good idea to request the file up front by loading it with a link in the head section of your HTML with the rel attribute value as preload. For example:
```html

<link
  rel="preload"
  href="fonts/inter.var.woff2"
  as="font"
  type="font/woff2"
  crossorigin
/>

```
- 