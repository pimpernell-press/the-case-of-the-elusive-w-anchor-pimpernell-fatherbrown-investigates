# Chapter 1: The Crime Scene Survey

*In which Father Brown examines a website that points to the wrong place,
and Flambeau discovers that "helping" is not always helpful.*

---

Father Brown did not, as a rule, investigate websites. He investigated souls,
which he found considerably better documented. But when Flambeau placed a
laptop before him in the vestry of St. Ambrose's and said, "Look at this,
Father — someone's stolen a man's front door and replaced it with a picture
of someone else's front door," even Father Brown had to admit the metaphor
was compelling.

The television in the corner of the vestry was on, as it always was — Mrs.
Hennessy left it running for company during the day. The South Bank Show
was playing — a repeat, or a special, or one of those extended editions
Melvyn Bragg did when he had something he couldn't fit into an hour. A
voice Father Brown didn't recognise was saying: "When I pay attention to
something beautiful, that attention was traditionally understood as a form
of love. Now it's harvested, quantified, and sold back to us as content."
Father Brown did not look at the screen. But he heard Melvyn Bragg reply,
with the careful neutrality of a man who has been asking questions for
forty years: "But surely people have always influenced each other's
thoughts?" The first voice said: "The scale and the sophistication,
certainly. But more fundamentally, the transformation of attention from
a gift into a resource."

The domain in question was `w-anchor.co.uk`. It belonged to a man named
Roger, who had registered it through a company called Heart Internet, which
was owned by a larger company called Host Europe Group, which was owned by
a still larger company called GoDaddy, which was owned — Father Brown
suspected — by the general principle that small fish exist to be eaten by
slightly less small fish, who exist to be eaten by fish so large they have
ceased to identify as fish and now refer to themselves as "the ocean."

"The curious thing," said Father Brown, peering at the screen with the
expression of a man examining a forged relic, "is not that the domain
points to the wrong place. Domains are like sheep — they wander. The
curious thing is *where* it wanders to."

He turned the laptop so Flambeau could see.

"It points to a parking page. A page that says, in effect, 'This domain
is available for purchase.' But it is *not* available for purchase. Roger
owns it. Roger has paid for it. Roger has the receipt."

"So someone put up a 'For Sale' sign on a house that isn't for sale,"
said Flambeau.

"Worse," said Father Brown. "Someone put up a 'For Sale' sign on a house
that isn't for sale, and when the owner complained, they told him the sign
was *for his benefit*."

---

## The Evidence Board

Flambeau, who had a detective's instinct for pinning things to walls, laid
out the facts:

**The Domain:** `w-anchor.co.uk`
- Registered to Roger via Heart Internet
- Paid up. Not expired. Not in dispute.

**The Problem:** Instead of showing Roger's website, the domain displayed
a GoDaddy parking page — a generic placeholder suggesting the domain was
unclaimed, often decorated with third-party advertisements from which
GoDaddy collected revenue.

**The Timeline:**
- Roger notices the redirect
- Roger contacts Heart Internet
- Heart Internet says it's a Nominet issue
- Nominet says it's a Heart Internet issue
- Roger contacts both again
- Both say the other one did it
- Roger begins to feel like a man trying to report a burglary to two
  police forces, each of which insists the crime occurred in the other's
  jurisdiction

"This," said Father Brown, folding his hands, "is what I call the
*Jurisdictional Waltz*. It is danced in three-quarter time, and it ends
only when the complainant runs out of stamps."

---

## The DNS Records

Father Brown had asked a technically-minded parishioner — a young woman
who ran the church website and who Father Brown privately considered a
kind of digital sacristan — to examine the domain's DNS records.

"Think of DNS," Father Brown explained to Flambeau, who was looking
apprehensive, "as the postal system of the internet. When someone types
`w-anchor.co.uk`, the DNS system looks up the address and sends them to
the right building. What we have here is a case where someone has gone
into the post office and changed the forwarding address."

The records showed:

- The domain's nameservers had been changed
- They now pointed to GoDaddy's parking infrastructure
- The change had not been requested by Roger
- The change had not been authorised by Roger
- Nobody could explain who had made the change, or when, or why

"In a just world," said Father Brown, "this would be called *theft*.
In the world of domain registration, it is called a *technical issue*."

Flambeau stared at the evidence. "So someone — either Heart Internet,
GoDaddy, or Nominet — changed the address without permission, and now
they're all pointing at each other?"

"Precisely," said Father Brown. "And while they point at each other,
they are all collecting rent on the parking page. It is a very modern
arrangement. In the old days, thieves at least had the decency to run
away from the scene of the crime. These days, they set up a
refreshment stand."
