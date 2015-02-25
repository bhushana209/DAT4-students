Excellent job Austin, this is shaping up to be a great project! Some comments:

- The number one thing I would encourage you to do is to continue to look closely at your data, at all steps of the data processing pipeline. That's because there are so many things that can go wrong, and these problems can be hard to detect without close investigation:
    - Do routes ever change? To what extent would that affect your data?
    - What happens when a bus breaks down? How will that be reflected in your data?
    - Do the APIs always provide "valid" data? Are they ever giving you back "bad data" (meaning ridiculous values) or missing values?
    - Does the API continue to serve up good and complete data, even when you are hitting it hard? (They have given you an API key with a higher limit, so theoretically it should work, but does that higher limit work in practice?)
    - Once you do your merge (as we talked about last night), are you doing it properly? Do the things that are supposed to match actually match? (We would hope that one API doesn't tell you a bus is "28B" and another says it's "28 B" and another says it's "28B ", but all of those are possible.)

- Besides just "looking closely" at your data, my number one tip for detecting problems is to make a list of your assumptions, and then test those assumptions. (You can even code up those assumptions as a function using `assert` statements, so that you can run it every time you generate some additional data!) Here are some examples:
    - In a given day, a given bus/stop combination should appear no more than X times in the dataset.
    - For a given bus/stop combination, two arrivals should be at least X minutes apart.
    - Column X should have a value of no less than Y and no greater than Z.
    - Column X should have at least Y unique values but no more than Z unique values.
    - Column X should never have a negative value.
    - If I pull down data during rush hour, I should get about X unique buses and Y unique stops. If I pull down data during off-peak hours, I should get about W buses and Z stops. (Use your domain knowledge!)
    - Etc.

- I like how you've set up your presentation so far! It's great that you are going to be talking about how you collected the data, because in your case, figuring out how to generate your dataset with a "meaningful" structure is one of the hardest parts of the project. This is super useful to share with your classmates!

- Great documentation of what you are doing and why, and excellent code comments.
