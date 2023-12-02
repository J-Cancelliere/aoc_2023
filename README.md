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
<strong>Day 1</strong>: This isn't so hard... D'oh!
</summary>
<p></p>
<p><strong>Part 1:</strong> Started out strong for part 1 of this puzzle! I coded my tests and functions, then got the right answer on my first attempt. My strategy was to iterate over each string both forwards and backwards simultaneously and record the first encountered number. This worked perfectly. What a great beginning to AOC! I'm sure part 2 will be just as easy, fun, and fulfilling...</p>
<p><strong>Part 2:</strong> <em>"Oh look at that! Some of the numbers are spelled out as words. No worries, <code>string.replace()</code> to the rescue! Perfect, all my tests are passing. Time to submit my answer and get my second star..."</em>
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
<strong>Day 2</strong>: Early morning cubes
</summary>
<p></p>
<p><strong>Part 1:</strong> I'm up early today (like, really early). Early enough to start today's puzzle as soon as it's released. Let's do this! After reading the instructions and peeking at the input data, I breath a sigh of relief. This is looking a bit easier compared to yesterday's wonky-words-number-nonsense. </p>

<p>I write my tests and my code. I'm using a dictionary to map the colors to the limits provided in the instructions, and I parse the input data into lists. I go over each list and compare the values with the mapped limits and calcualte the count of possible games. Everything looks good and I submit my answer... oh dear, I've already failed my first submission.</p>

<p>I take another look at the instructions. Whoops! I've calculated the <em>count of games</em>, but the puzzle instruction is asking for the <em>sum of the game IDs</em> (sigh). I'm up too early and am too tired; I didn't read through all the instructions... After some reworking of my dictionary keys (*cought* and my unit tests *cough*), my second submission is successful. Phew!</p>

<p><strong>Part 2:</strong> Finding the lowest possible values in the games for each color is easy enough to solve (after <em>triple checking</em> the instructions for part 2). I set about finding the highest value in my lists from part 1. Once I have a dicitonary for each color containing the numbers, I code another function to multiply the three numbers together. I apply these functions to the entire input list and sum the products. Success!</p>

<p>Day 2 is done and dusted. What did I learn today? <strong>Read the instructions</strong>! And maybe have a coffee before trying to start coding at 5:00 AM. Also, don't forget to <strong>read the instructions</strong>!</p>
</details>


<!--
-- New day template --
<details>
<summary>
<strong>Day {n}</strong>: {headline}
</summary>
<p><strong>Part 1:</strong></p>
<p><strong>Part 2:</strong></p>
</details>
-->
