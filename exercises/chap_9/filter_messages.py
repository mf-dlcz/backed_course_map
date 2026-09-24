"""
FILTER MESSAGES:

We need to filter the profanity out of our game's live chat feature! Complete the filter_messages function. 

It takes a list of chat messages as input and returns two new lists:

A list of the same messages but with all instances of the word dang removed.

A list containing the number of dang words that were removed from each message at that particular index.
Here are some examples:

messages = ["dang it bobby!", "look at it go"]
filter_messages(messages)  # returns ["it bobby!", "look at it go"], [1, 0]

messages2 = [
    "That's the bloody dang Reaper of Mars...",
    "Pax au Telemanus!",
    "I was never taught how to use a dang razor!",
]
filter_messages(
    messages2
)  # returns ["That's the bloody Reaper of Mars...", "Pax au Telemanus!", "I was never taught how to use a razor!"], [1, 0, 1]


INSTRUCTIONS:

1. Create the two empty lists that you'll return at the end:
    a. One for the filtered messages with "dang" removed.
    b. And one for the counts of "dangs" removed from those messages.

2. Loop over the list of messages. For each message:
    a. Split the message string into a list of words using the .split() string method.
    b. Create an empty list for all the good words in this message.
    c. Create a counter variable for the "dangs" in this message, starting at 0.
    d. For each word in the message:
        a. If the word is "dang", add 1 to the "dangs" counter.
        b. If the word is not "dang", add it to the list of good words.
    e. Join the list of good words into a single string using the .join() method.
    f. Append the new filtered message to the list of filtered messages.
    g. Append the new "dangs" count to the list of counts of "dangs."

    3. After looping over the list of messages, return the list of filtered messages first, then the list of "dang" counts.


"""

