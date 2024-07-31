# How do u make the code:
- ### Readable to Humans?
- ### Easy to change?

I want to focus in the "Easy to Change" part as i think is the most complicated topic, the readable part come after that.

---
# Easy to change
The idea that's bugging me for a lot is code with options.
Description:
1. Make a simple code which other code refers to and can add to or **change**.
2. Write **options** or other **functions** that adds to your code.
3. These **options** have to be added to your code via a function or method, so i know whats happening.

###### ~Ex.:
Let's say you created a function that does some calculation in a for-loop and adds to a value `tot` at each iteration of the for-loop, normally i get in output of the function just the `tot` at the end, without actively changing the function how can i get in return all the value `tot` assumed during the function call.

Can i create "an **option**", some other code that can refer to the function and return what i asked for.

One idea i had is the [[Python - Idea 'Code Anchors'|Code Anchors]], but i dont like the flavor.
- Practically, you can add line of codes like labels that you can attach functions to: `code_anchor INITIALIZATION`.
- If developed further you can automate the label structure, creating some automatic ones like: `INITIALIZATION`, `FOR_LOOP_1`, `FOR_LOOP_2`, `WHILE_LOOP_1`, and so on.
- I would like to introduce 3 new python keywords: `code_anchor`,  `add_code_to` and `at`, where `at` can be used only in `add_code_to` block.
- Then using Sublime Text as IDE I would like to create a [[Sublime Text - Phantoms|phantom]] every time i create a `add_code_to` block under that a grey-code of the function or class it refers to, where the `code_anchor` keyword is replaced by the `at` keyword.

**Idea**: Create a normal function, then pass it to a function or class `add_options_to_function(func, **options)`, to add options

