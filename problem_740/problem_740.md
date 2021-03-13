Secret Santa is a process that allows people to give each other presents, so that each person gives a single present and receives a single present. At the beginning each of the n people write their name on a slip of paper and put the slip into a hat. Each person takes a random slip from the hat. If the slip has their name they draw another random slip from the hat and then put the slip with their name back into the hat. At the end everyone buys a Christmas present for the person whose name is on the slip they are holding. This process will fail if the last person draws their own name.

In this variation each of the n people gives and receives two presents. At the beginning each of the people writes their name on two slips of paper and puts the slips into a hat (there will be 2n slips of paper in the hat). As before each person takes from the hat a random slip that does not contain their own name. Then the same person repeats this process thus ending up with two slips, neither of which contains that person's own name. Then the next person draws two slips in the same way, and so on. The process will fail if the last person gets at least one slip with their own name.

Define q(n) to be the probability of this happening. You are given q(3) = 0.3611111111 and q(5) = 0.2476095994 both rounded to 10 decimal places.

Find q(n) rounded to 10 decimal places.

So for 1 people, let's start at the beginning. At each step we want to work out the probability of at least 1 slip of paper with person n's name still being in the draw. Forget separating it by people! There's nothing against 1 person getting the same person twice as long as it's not them!

So, on pass 1, P_1, the chances, P(1) of person n's name being pulled out is 2/2n = 1/n.
On P_2, this becomes P(2) = P(1)(1/2n-1) + (1-P(1))(2/2n-1)
P(3) = P(1)P(2)x0 + P(1)(1-P(2))(1/2n-2) + (1-P(1))(P(2))(1/2n-2) + (1-P(1))(1-P(2))(2/2n-2)
P(4) = SUM(all combinations where only one has happened)(1/2n-3) + product(none having happened)(2/2n-3)

I smell a binomial of all things...

P(r) = SUM(all combinations where only one has happened)(1/1+2n-r)) + (none having happened)(2/1+2n-r)

I think store it as an array/list/whatever it is the language in question calls it.
Actually 2, 1 for the negative probabilities. Well, not negative *probabilities* but, yeah, you get what I mean.

We now need the chances of it happening less than twice by P(2n-2)

P(1) = 1/2n + 1/2n-1
P(2) = 1/2n-2 + 1/2n-3
P(3) = 1/2n-4 + 1/2n-5
...
P(x) = 1/2n-(2x-2) + 1/2n-(2x-1)
...
P(n-2) = 1/2n-(2(n-2)-2) + 1/2n-(2(n-2)-1) = 1/6 + 1/5
P(n-1) = 1/2n-(2(n-1)-2) + 1/2n-(2(n-1)-1) = 1/4 + 1/3