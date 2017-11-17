import scrapy
from spider_utils import *

util = SpiderUtils()

class AljazeeraSpider(scrapy.Spider):
    name = "aljazeera"



    def start_requests(self):
        urls = ['http://www.aljazeera.com/news/2017/11/donald-trump-asia-pacific-challenges-171103130933273.html']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        #text = response.xpath('// *[ @class ="article-p-wrapper"]//*/text()')
        #blob = text.extract()

        nlppl = util.pipeline(response)

        #print(nlppl)

        #print(blob)
        #yield st




        #for text in response:
            #yield { text: text }
            #print(text)



        # page = response.url.split("/")[-2]
        # filename = 'aljazerra-%s.html' % page
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log('Saved file %s' % filename)

a = AljazeeraSpider()
response = ['New York City', ' - ', 'U.S.A. and i.e. Donald Trump', "'s upcoming tour of Asia offers plenty to keep the US president cheerful, from lavish state banquets to honour-guard pomp and even a chummy round of golf with Japanese Prime Minister ", 'Shinzo Abe', '.', "That's where the fun stops. It also represents a gruelling 12-day slog of speech-making, summits, and tricky sit-downs on a range of trade disputes - and the intractable policy headache of North Korea's ", 'nuclear arms programme', '.', 'These are big tests for a commander-in-chief who does, on occasion, follow the teleprompter and stay "on message", but at other times becomes frustrated and fires off salvos of brusque, early morning ', 'Twitter', ' missives.', 'Before Air Force One takes off for a Hawaii visit on Friday, Al Jazeera picked out the key challenges facing Trump on an odyssey that starts in ', 'Japan', ' on Sunday before stops in ', 'South Korea', ', China, Vietnam and the ', 'Philippines', '.', 'North Korea', 'The way the Trump administration tells it, the totalitarian regime in Pyongyang is rapidly developing nuclear warheads and the intercontinental ballistic missiles to carry them to a US West Coast city such as Seattle or Los Angeles.', '\r\n', '{articleGUID}', '\r\n', "The White House counter-strategy seems to be assuring allies such as South Korea and Japan that the US still has their back, while getting North Korea's main ally, ", 'China', ', to economically pressure Pyongyang back to the bargaining table.', 'Chinese President ', 'Xi Jinping', "'s calculus is different. Beijing-Pyongyang relations have troughed, but a collapse of the hermit nation could send refugees spilling northwards and land American troops on China's doorstep.", "That's a recipe for trouble at Trump-Xi talks from November 8 onwards, Leland Miller, cofounder and CEO of China Beige Book, a data consultancy on the world's second-biggest economy, told Al Jazeera.", '"Many Trump administration officials believe that Beijing has to help solve the North Korea problem. Not be helpful, but solve the problem. And there\'s no easy solution to this, certainly not one that China will find acceptable and low cost," Miller said.', 'US-China relations\xa0', 'Trump\'s stop in Beijing is being billed as a "state visit plus" to mark the importance of the dynamic between himself and President Xi, as well as relations between the US superpower and China\'s fast-growing economy and armed forces.', 'North Korea', ' is not the only glitch. Trump rails against the United States\' "embarrassing" $347bn trade deficit with China, and has accused Beijing of manipulating its currency, rigging markets, and pilfering ideas from US firms.\xa0', 'According to Miller, the two leaders may be able to paper over the cracks by unveiling a few energy deals this month, but that would only be a "calm before the storm" and the "escalation of tensions" next year.', '"The Trump administration has high expectations from China, a fundamental reordering of the trade relationship, while China expects a relatively painless negotiation process," Miller said.', 'Meanwhile, the two leaders are in different positions. Xi has just emerged from a glowing five-yearly Communist Party congress; Trump has ', 'low approval ratings', ' of 34 percent and is battling a probe about election ', 'collusion', ' with Russia.', 'Former CIA analyst Christopher Johnson compared Xi\'s "strong position with no visible domestic opposition" to Trump\'s routinely questioned style and legislative record. ', '"This gives Xi a bit of a leg up" when bartering, Johnson told Al Jazeera.', 'New Asia-Pacific policy', 'Former US President ', 'Barack Obama', ' tried to "rebalance" the US\' defence and economic policy to counter China\'s rise, including with a 12-nation Trans-Pacific Partnership (TPP) trade deal that excluded Beijing.', 'Trump scrapped TTP almost as soon as he entered the White House in January.', '\r\n', '\r\n', 'Amy Searight, a former ', 'Pentagon', ' official, told Al Jazeera the "lack of any replacement with a proactive trade policy or economic agenda" has left Washington\'s Asian partners feeling anxious.', 'The property magnate is expected to unveil a new framework at the Asia Pacific Economic Cooperation (APEC) summit in Da Nang, ', 'Vietnam', ', on November 10. White House officials talk up plans for a "free and open Indo-Pacific region".', 'Although big questions about the policy remain, a recommitment to rules-based economic fairness may be a solid message, Lindsey Ford, a former Department of Defense official, told Al Jazeera.\xa0', '"It\'s important for people to hear that America First does not mean Asia last; that American prosperity can go hand in hand with Asian prosperity," said Ford, an analyst at the Asia Society Policy Institute, a think-tank.', 'Keeping allies sweet', "The first two stopovers are Washington's key allies in Northeast Asia: Japan and South Korea. They have both been rattled by a wildcard president who threatened to upend a global order the US had underpinned for decades.", 'Trump has spoken of raining "fire and fury" on North Korea - rhetoric that nudges the region towards a potentially calamitous conflict. He may well tone that down a notch when addressing the National Assembly in Seoul on November 8.', 'He may also be wise to offer some goodies. The United States\' pull-out from TPP came as China was rolling out its multibillion-dollar "Belt and Road" infrastructure development plan across Asia and beyond.\xa0', 'According to Ford, the expected Asia policy must provide a new "economic vision, post-TPP". Simply renegotiating a bilateral trade with South Korea, and vaunting new ones with Japan and Vietnam, is not enough.\xa0', 'Trump being Trump\xa0', "Trump's biggest challenge could be the one thing he cannot seem to change: himself.\xa0", 'He is prone to undiplomatic language that plays badly with buttoned-down Asian officials. Previously on Twitter, he accused South Korea of trying to "appease" its northern neighbour, and criticised Xi for not doing enough to rein in Pyongyang.', '\r\n', '{articleGUID}', '\r\n', 'The trip is longer and tougher than his first foreign venture to the ', 'Middle East', ' in May. He may get irked by Japanese resentment over a US military base in Okinawa, or rallies against the "war maniac" US president on the streets of South Korea.', '"Among government officials, there are going to be a lot of white-knuckles and held breath throughout the two days of his time in South Korea," Scott Snyder, a scholar at the Council on Foreign Relations, a think-tank, told Al Jazeera.\xa0', 'There is a risk of clashing egos when Trump meets ', 'Rodrigo Duterte', ', the hard-boiled president of the Philippines, on November 13. Meanwhile, Russian President ', 'Vladimir Putin', ' will attend APEC, shifting the spotlight back on to the troublesome probe of election collusion.', 'China is a safer bet, said Elizabeth Economy, author of The Third Revolution, a book about modern China. ', 'Thanks to a government block on Twitter, Trump\'s time there could "turn out to be 36 hours of drama-free [from] tweeting," she told Al Jazeera.', 'Follow James Reinl on Twitter: ', '@jamesreinl']

a.parse(response)