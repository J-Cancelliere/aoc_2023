<h1 style="text-align: center;"> 🎅🎄❄️ Merry Code-mas! ❄️🎄🎅</h3>

<p>This repo contains all my solutions for the 2023 <a href=https://adventofcode.com/2023>Advent of Code</a> puzzles. This is my first year doing AOC, and I'll be using Python as my language of choice. 🐍</p>

<p>This repo is split into two main directories: <code>test_aoc</code> and <code>challenges</code>:</p>
<ul>
<li><strong>test_aoc</strong> contains all the unit tests I write for every puzzle. Each day's puzzle will contian its own script following this naming convention: <code>test_{day}.py</code></li>
<li><strong>challenges</strong> is where I write one module for every day's puzzle.</li>
</ul>

<p>As I go through the puzzles, I'll be documenting my experience and lessons learned in this README. Keep your eyes on this space as I update with each day's puzzle update!</p>

<details>
<summary>
<strong>Day 1</strong>: This isn't so hard... D'oh! 👨‍💻🙃
</summary>
<p></p>
<p><strong>⭐ Part 1:</strong> Started out strong for part 1 of this puzzle! I coded my tests and functions, then got the right answer on my first attempt. My strategy was to iterate over each string both forwards and backwards simultaneously and record the first encountered number. This worked perfectly. What a great beginning to AOC! I'm sure part 2 will be just as easy, fun, and fulfilling...</p>
<p><strong>⭐ Part 2:</strong> <em>"Oh look at that! Some of the numbers are spelled out as words. No worries, <code>string.replace()</code> to the rescue! Perfect, all my tests are passing. Time to submit my answer and get my second star..."</em>
<ol>
<li><strong>First attempt</strong>: I map all the words to digits and naively use <code>str.replace()</code> to modify the string before reusing my funtion for part 1. Submission failed. I do some searching and realize it's due to edge cases in the input ("oneight", "sevenine", etc)</li>
<li><strong>Second attempt</strong>: Okay, so <code>str.replace()</code> is a bust. Let's use <code>str.find()</code> to get the index of the words and amend the strings this way. I add the digit to the beginning of the word in the string, but this doesn't fix all the issues (think "on8eight" or "seve9nine"). Failed again.</li>
<li><strong>Third attempt</strong>: That's an easy fix! I rework the function to insert the digit inside the existing word so that I catch everything ("o1ne8ight", "s7even9ine"). Submission still failing!? I'm start to unravel. Time for a break before I come back to reassess.</li>
<li><strong>Fourth attempt</strong>: Turns out I didn't account for the fact that <code>str.find()</code> only finds the first instance of a word and doesn't keep finding. I set up a <code>while</code> loop to continue finding all instances of a word, so if a word is repeated ("twotwo"), both of them get a digit ("t2wot2wo"). FINALLY, I've clawed my way to that second star. </li>
</ol></p>
<p>So I finish the first day of AOC feeling a mix of relief and pride at having completed the puzzle (along with a hefty dose of embarassment for how long it took; have I really become this rusty at Python?). The main lesson learned? <strong>Think harder about my tests</strong>. I defintiely did not cover enough edge cases before trying to submit my part 2 solutions. Anxiously awaiting day 2's puzzle with some slight trepidation now...</p>
</details>

<details>
<summary>
<strong>Day 2</strong>: Early morning cubes 🌅🧊
</summary>
<p></p>
<p><strong>⭐ Part 1:</strong> I'm up early today (like, really early). Early enough to start today's puzzle as soon as it's released. Let's do this! After reading the instructions and peeking at the input data, I breath a sigh of relief. This is looking a bit easier compared to yesterday's wonky-words-number-nonsense. </p>
<p>I write my tests and my code. I'm using a dictionary to map the colors to the limits provided in the instructions, and I parse the input data into lists. I go over each list and compare the values with the mapped limits and calcualte the count of possible games. Everything looks good and I submit my answer... oh dear, I've already failed my first submission.</p>
<p>I take another look at the instructions. Whoops! I've calculated the <em>count of games</em>, but the puzzle instruction is asking for the <em>sum of the game IDs</em> (sigh). I'm up too early and am too tired; I didn't read through all the instructions... After some reworking of my dictionary keys (*cough* and my unit tests *cough*), my second submission is successful. Phew!</p>
<p><strong>⭐ Part 2:</strong> Finding the lowest possible values in the games for each color is easy enough to solve (after <em>triple checking</em> the instructions for part 2). I set about finding the highest value in my lists from part 1. Once I have a dicitonary for each color containing the numbers, I code another function to multiply the three numbers together. I apply these functions to the entire input list and sum the products. Success!</p>
<p>Day 2 is done and dusted. What did I learn today? <strong>Read the instructions</strong>! And maybe have a coffee before trying to start coding at 5:00 AM. Also, don't forget to <strong>read the instructions</strong>!</p>
</details>

<details>
<summary>
<strong>Day 3</strong>: Who needs a weekend? 3️⃣1️⃣2️⃣🔍
</summary>
<p></p>
<p><strong>⭐ Part 1:</strong> Today's puzzle was a tough one, and we're only on day 3! I spent far too much time trying to figure this out and had to walk away and come back multiple times to avoid giving up entirely.</p>
<p>My first idea was to create a dictionary containing each line with the row index as the key. I then wrote some for loops to search the sides, above, and below numbers. I encountered a lot of issues with indices being out of range (<em>literal</em> edge cases). After a failed first submission, I change strategy: extract a list of numbers from the line first. Then I find the index of each number. I expand the search field from that index to include left, right, above, and below. I also have to figure how to deal with edge cases again. I fail submission yet again.
</p>
<p>Turns out there's a problem is with <code>str.find()</code> (have I not learned my lesson in day 1?) I check for duplicates in the number list and work around the issue using <code>str.rfind()</code>. And my submission fails <em>again</em>! Time to step away from the computer and going out for a bit.
</p>
<p> I'm back from brunch and a bit more motivated. I've decided to scrap everything and start over, working with numpy this time. I split every character out into a list. This is used to create a numpy array (I've also added a row of padding along all the sides; edge cases no more!). I write a function to create a "window" surrounding each number. Once all the windows are created, I flatten each array and look for any punctuation. Finally succeeded on this one! Though I'm dreading part 2 now.</p>
<p><strong>⭐ Part 2:</strong> At this point in the day. My brain is fried. I try working with my existing code to come up with an easy solution, but it's getting late and I think I've sacrificed enough of my sunday to AOC.</p>
<p>After several feeble attemps with no tangible results. I go searching in the AOC subreddit for inspration. I find another python solution and cobble it into my module. If the main reason for doing AOC is to learn, I think part of that process is learning to read and implement other people's code as well. You can't always have all the answers! Here's to hoping for a more relaxed Monday puzzle.</p>
</details>

<details>
<summary>
<strong>Day 4</strong>: A lifetime supply of scratchoffs! 🎟️🎫🎟️
</summary>
<p></p>
<p><strong>⭐ Part 1:</strong> I didn't have too much trouble coding today's part 1. A nice change from yesterday. To parse the input data, I split the strings into a dictionary. Each key, value pair has the card as a key and a tuple with 3 items (winners, numbers, point value) as the value.</p>
<p> I loop over each set of numbers, and then nest another loop to check for the winners. If the difference between the number and the winning value is 0, it's a match and I update the point value accordingly. All that's left now is to sum all the point values from the tuples as I check all the cards. Voilà! Part 1 done.</p>
<p><strong>⭐ Part 2:</strong> It turns out we win more cards for all winning cards. <em>Great</em>. I increase the tuple to include more parameters (5 altogether, adding the match count and number of cards). I run two more loops through the cards: one loop to update matches, and one loop to update copies. This takes a while to run, but is works, so I'll take the win.</p>
</details>

<details>
<summary>
<strong>Day 5</strong>: Reaching my limit (of RAM) 🌱🤯
</summary>
<p></p>
<p><strong>⭐ Part 1:</strong> My first idea for this challenge was to create a dictionary with all the mappings for each seed's values. It was fine with the test data, but then I realised the actual input would require way too much memory for this approach. I switched approcahes and did comarisons between the source and destination values to get all the mappings correct. I run my code and earn another star, but it's the only star I'll earn today...</p>
<p><strong>❌ Part 2:</strong> Did not finish. I reworked my code given the criteria for part 2, and all my tests are passing. Unfortunately my code is very inefficient and running it on the full input data results in a killed script due to memory limits. I'll have to do some more in depth research on this one later, but I'm done for now. Tomorrow is another day!</p>
<p><strong>⭐ Update!</strong> After implementing my day 6 solutions, I came back to my day 5 code to try and figure out a way to get my script to run. It's not pretty (honestly, it's hideous), but now I have a working script that runs... <em>for over 12 hours</em>. I was aware of term "brute force" before this, but now I've experienced it firsthand. This is defintiely the most inefficient thing I've ever coded, but it worked!! Feeling a bit silly for putting my CPU through this, but now I have my second star. </p>
<p>The upside to this code monstrosity? I've got something I can come back to later on as a little project. Some day I will come back to this script and figure out a way to make it run in a reasonable amount of time (<em>is 4 hours too much to ask for!?</em>).</p>
</details>

<details>
<summary>
<strong>Day 6</strong>: A day at the boat races ⛵🏁
</summary>
<p></p>
<p><strong>⭐ Part 1:</strong> Today was a real confidence boost after missing out on part 2 of yesterday. In the test data that there is a range of timings for holding the button that will allow you to win, so I decide to search for the lower and upper bounds of this range with two loops. One searched forwards until it finds the lower limit, and the other searches backwards until it hits the higher limit. Tada! Solution found.</p>
<p><strong>⭐ Part 2:</strong> So it turns out the input isn't a series of races, but one big number for one race. At this point, I'm feeling really good that I thought to optimise my search function a bit during part 1! I adjust my parsing to make a single number for both the time and race numbers. I run the same search on this big number and get the right result on the first try. I was so excited to implement part 2 that I forgot to even write any tests.</p>
<p>My part 2 solution does take a few seconds to run, so it's not the most efficient code. However, I think that a week ago I would have written a much more inefficient function to solve this problem. This day's puzzle definitely has shown me that I'm improving my coding skills, so I'm going to keep up with AOC as long as I can. Looking forward to day 7 now!</p>
</details>

<details>
<summary>
<strong>Day 7</strong>: More card games ♣️ ♦️ ♠️ ♥️
</summary>
<p></p>
<p><strong>⭐ Part 1:</strong> Today's puzzle was an interesting one, and I learned a lot of great things. The toughest part of this one was figuring out what type of hand each set of cards was. After lots of <code>if</code> conditions in my first function, I coded a quicksort algorithm and applied it to each batch of types. After that, it was just a matter of looking up the bet value to multiply by my list order.</p>
<p><strong>❌ Part 2:</strong> I got a late start on these challenges today, so by the time I was trying to sort out the switch from "Jack" to "Joker", I was already sleepy. I tried modifying my original functions to work in the same way, but my first submitted answer was too high. I decided to give myself a break and whent to bed.</p>
<p><strong>⭐ The next morning</strong>: With a fresh set of eyes, I set about figuring out part 2. I decided to switch up my original function to return a dictionary for hand types instead of the sorted list. This let me create a new funtion that identifies all "J" characters and then recategorises them into the correct types. Then I resort the lists, concatenate then, and apply my winnings calculation again. Success! Now time for breakfast.</p></p>
<p>One peculiar thing about this solution is that my unit tests are mostly failing now (oops). This AOC is one of the first times I've written my own unit tests, so I suppose it's expected that I won't write perfect tests all the time. I may come back to these tests at some point to rework them to learn how I could have written them better.</p>
</details>

<details>
<summary>
<strong>Day 8</strong>: Lost in the haunted desert 🏜️🐪👻
</summary>
<p></p>
<p><strong>⭐ Part 1:</strong> This was a fairly straightforward looping solution. I got stuck for a bit on my step_limit variable when I set it too short, making infinite loop. I just kept watching my loop spin and spin for about 5 minutes before I figured out which part wasn't working. Otherwise, I implemented my solution pretty quickly.</p>
<p><strong>⭐ Part 2:</strong>If iterating worked for part 1, it would be the same for part 2, right? I write a new <code>while</code> loop to iterate over all the paths at once and let it run. Then the script just kept runnnig. After doing some research, I came across the least common multiple approach and decided to implement this while my iterative script kept running.</p>
<p>The biggest challenge of this approach was finding the paths, since there are multiple starts and multiple fininshes. I add a timeout condition to my original step counting function so when I try all the combinations, if there's an infinite loop for any of them, it stops after 1 second. After implementing this solution I have my answer, and the number is much higher than my slow scipt ever got. <em>They say if you listen closely, you can still hear that other script iterating on and on forever...</em></p>
</details>

<!--
-- New day template --
<details>
<summary>
<strong>Day {n}</strong>: {headline}
</summary>
<p></p>
<p><strong>Part 1:</strong></p>
<p><strong>Part 2:</strong></p>
</details>
-->
