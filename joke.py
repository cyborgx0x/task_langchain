from langchain.prompts import ChatPromptTemplate
from llm_gpt import CustomLLM
from local_model import llm
# model = CustomLLM(n=1)
model = llm

google_search_data = {
    "searchParameters": {
        "q": "2 Casino Ransomware Attacks: Caesars, MGM",
        "num": 20,
        "type": "search",
        "engine": "google"
    },
    "organic": [
        {
            "title": "2 Casino Ransomware Attacks: Caesars Paid, MGM Did Not - Forbes",
            "link": "https://www.forbes.com/sites/suzannerowankelleher/2023/09/14/2-casino-ransomware-attacks-caesars-mgm/?sh=552604b2402d",
            "snippet": "The House Loses: Caesar's Entertainment paid a ransom after being cyberattacked. getty. Within weeks, two of the world's largest casino-hotel ...",
            "date": "Sep 14, 2023",
            "position": 1
        },
        {
            "title": "Hackers who breached casino giants MGM, Caesars also hit 3 other firms, Okta says",
            "link": "https://www.reuters.com/technology/hackers-who-breached-casino-giants-mgm-caesars-also-hit-3-other-firms-okta-says-2023-09-19/",
            "snippet": "The hacks have cast fresh spotlight on ransomware attacks - cyber intrusions that affect hundreds of companies every year, from healthcare ...",
            "date": "5 days ago",
            "position": 2
        },
        {
            "title": "Las Vegas casino ransomware attacks: Okta in the spotlight as MGM slowly recovers",
            "link": "https://www.thestack.technology/mgm-okta-ransomware/",
            "snippet": "Caesar's said in a September 7 filing with the SEC that it had identified \u201csuspicious activity in its information technology network resulting ...",
            "date": "5 days ago",
            "position": 3
        },
        {
            "title": "Massive MGM and Caesars Hacks Epitomize a Vicious Ransomware Cycle - WIRED",
            "link": "https://www.wired.com/story/mgm-ceasars-hack-ransomware/",
            "snippet": "Cyberattacks on casinos grab attention, but a steady stream of less publicized attacks leave vulnerable victims struggling to recover.",
            "date": "Sep 16, 2023",
            "position": 4
        },
        {
            "title": "2 Casino Ransomware Attacks: Caesars Paid, MGM Did Not | Energy Central",
            "link": "https://energycentral.com/c/um/2-casino-ransomware-attacks-caesars-paid-mgm-did-not",
            "snippet": "Within weeks, two of the world's largest casino-hotel companies\u2014MGM Resorts and Caesars\u2014were hit with ransomware attacks. One met the hackers' ...",
            "date": "5 days ago",
            "position": 5
        },
        {
            "title": "Cyberattacks strike casino giants Caesars and MGM - NPR",
            "link": "https://www.npr.org/2023/09/15/1199681234/cyberattacks-strike-casino-giants-caesars-and-mgm",
            "snippet": "The disclosure by Caesars came after MGM Resorts International reported publicly that a cyberattack it detected led it to shut down computer ...",
            "date": "Sep 15, 2023",
            "position": 6
        },
        {
            "title": "MGM and Caesars hit with massive cyber attack - CNBC",
            "link": "https://www.cnbc.com/video/2023/09/15/mgm-and-ceasars-hit-with-massive-cyber-attack.html",
            "snippet": "Two major Las Vegas casinos were overcome by ...",
            "date": "Sep 15, 2023",
            "attributes": {
                "Duration": "1:11",
                "Posted": "Sep 15, 2023"
            },
            "imageUrl": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcTozgJcu3NtwLG1kumCLt1s23zwzmT0eqHiW2eyA0U5cxLb72mgs4D0zXlcWNI",
            "position": 7
        },
        {
            "title": "Caesars paid millions in ransom to cybercrime group prior to MGM hack - CNBC",
            "link": "https://www.cnbc.com/2023/09/14/caesars-paid-millions-in-ransom-to-cybercrime-group-prior-to-mgm-hack.html",
            "snippet": "Days before MGM's computer systems were taken down in a cyberattack, casino operator Caesars paid out a ransom worth $15 million to a cybercrime ...",
            "date": "Sep 14, 2023",
            "position": 8
        },
        {
            "title": "Caesars Paid Ransom After Suffering Cyberattack - WSJ",
            "link": "https://www.wsj.com/business/hospitality/caesars-paid-ransom-after-suffering-cyberattack-7792c7f0",
            "snippet": "MGM's casinos include Bellagio, Aria, MGM Grand and Mandalay Bay. MGM hasn't released further details about its cybersecurity issue, including ...",
            "date": "Sep 14, 2023",
            "position": 9
        },
        {
            "title": "Two Vegas casinos fell victim to cyberattacks, shattering the image of impenetrable casino security | AP News",
            "link": "https://apnews.com/article/vegas-casinos-mgm-caesars-cyberattack-59644d2cb0f2a765770d30f268b81a11",
            "snippet": "It's true, Kim said, that casino giants like MGM Resorts and Caesars are protected by sophisticated \u2014 and expensive \u2014 security operations.",
            "date": "Sep 15, 2023",
            "position": 10
        },
        {
            "title": "Over the past few weeks, MGM and Caesars were both hacked by one of the most 'aggressive threat actors' targeting the US - Fortune",
            "link": "https://fortune.com/2023/09/13/mgm-caesars-hacked-ransomware/",
            "snippet": "... MGM hotel and casino in ... casinos across the country, according to two of the people. Caesars was also hacked by the same group in a cyberattack ...",
            "date": "Sep 13, 2023",
            "position": 11
        },
        {
            "title": "Ransom Cyber-Attack Disrupts MGM and Caesars Casino Properties - Downbeach BUZZ",
            "link": "https://downbeachbuzz.com/ransom-cyber-attack-disrupts-mgm-and-caesars-casino-properties/",
            "snippet": "Two major casino operators still recovering from recent ransomware attacks. Computer systems at MGM were shut down, freezing slots machines, ...",
            "date": "6 days ago",
            "position": 12
        },
        {
            "title": "MGM Resorts computers back up; analysts eye effects of casino cyberattacks - ABC7",
            "link": "https://abc7.com/las-vegas-cyberattack-mgm-hotel/13810853/",
            "snippet": "\"There's been attacks against multiple casinos, and it's possible we'll see more.\" Caesars Entertainment is the largest casino owner in the ...",
            "date": "3 days ago",
            "position": 13
        },
        {
            "title": "Caesars admits it was hacked in second major Las Vegas casino breach: Company 'paid $15M ransom' to Scattered Spider gang that also crippled MGM's hotels and casinos - Daily Mail",
            "link": "https://www.dailymail.co.uk/news/article-12519147/Caesars-admits-hacked-second-major-Las-Vegas-casino-breach-Company-paid-15M-ransom-Scattered-Spider-gang-crippled-MGMs-hotels-casinos.html",
            "snippet": "In a regulatory filing on Thursday, Caesars said it had identified the breach by September 7, just days before a separate ransomware attack ...",
            "date": "Sep 14, 2023",
            "position": 14
        },
        {
            "title": "Caesars ransom attack linked to MGM, tens of millions paid to hackers - Cybernews",
            "link": "https://cybernews.com/security/caesars-palace-mgm-ransomware-attack-confirmed/",
            "snippet": "... ransomware attacks targeting Sin City's hotel and casino giants starting last month. MGM Resorts announced it had been hit by a cyberattack ...",
            "date": "Sep 14, 2023",
            "position": 15
        },
        {
            "title": "Lance Spitzner on LinkedIn: 2 Casino Ransomware Attacks: Caesars Paid, MGM Did Not | 12 comments",
            "link": "https://www.linkedin.com/posts/lancespitzner_2-casino-ransomware-attacks-caesars-paid-activity-7109901687556882432-x3mU",
            "snippet": "Great write-up from Forbes on the MGM and Caesar Ransomware attacks. Many people may not realize this but the vast majority of casinos in Las Vegas are ...",
            "position": 16
        },
        {
            "title": "Hackers tied to Las Vegas attacks known for sweet-talking their way into company systems",
            "link": "https://www.nbcnews.com/tech/security/mgm-las-vegas-hackers-scattered-spider-rcna105238",
            "snippet": "MGM Resorts, which runs many of the most popular casinos and hotels ... She declined to comment on who might be behind the recent casino attacks.",
            "date": "Sep 15, 2023",
            "attributes": {
                "Missing": "2 | Show results with:2"
            },
            "position": 17
        },
        {
            "title": "MGM, Caesars Cyberattacks a Threat to Operations\u2014and Stocks | Barron's",
            "link": "https://www.barrons.com/articles/mgm-caesars-stock-cyberattacks-hackers-422b2a3a",
            "snippet": "Investors should get used to it amid a boom in ransomware attacks and new measures to increase transparency from companies. MGM Resorts ...",
            "date": "Sep 14, 2023",
            "position": 18
        },
        {
            "title": "MGM reeling from cyber 'chaos' 5 days after attack as Caesars Entertainment says it was hacked too - ABC News",
            "link": "https://abcnews.go.com/Business/mgm-reeling-cyber-chaos-5-days-after-attack/story?id=103148809",
            "snippet": "2:08. Las Vegas hotels still reeling from cyberattack. A shadow ... PHOTO: An exterior view of MGM Grand hotel and casino, after MGM Resorts shut.",
            "date": "Sep 14, 2023",
            "position": 19
        },
        {
            "title": "Caesars confirms data theft as MGM casino outage drags on \u2022 The Register - Theregister",
            "link": "https://www.theregister.com/2023/09/14/caesars_mgm_hacks/",
            "snippet": "\u201cAfter waiting a day, we successfully launched ransomware attacks against more than 100 ESXi hypervisors in their environment on September ...",
            "date": "Sep 14, 2023",
            "position": 20
        }
    ],
    "peopleAlsoAsk": [
        {
            "question": "How much did MGM lose from cyber attack?",
            "snippet": "MGM losing up to $8.4M per day as cyberattack paralyzes slot machines, hotels for 8th straight day: analyst. They also appear to make the effort to study how large organizations work, including their vendors and contractors, to find individuals with privileged access they can target, according to analysts.",
            "title": "Gen Z Hackers behind MGM , Caesars breaches 'more sophisticated ...",
            "link": "https://nypost.com/2023/09/22/gen-z-hackers-behind-mgm-caesars-breaches-more-sophisticated-ruthless/"
        },
        {
            "question": "Is MGM still under cyber attack?",
            "snippet": "MGM Resorts' hotels and casinos are back up and running normally following last week's cyber incident, the company said Wednesday in a post on X, the social media site formerly known as Twitter.",
            "title": "MGM Resorts says hotel, casino operations back up and running",
            "link": "https://www.cybersecuritydive.com/news/mgm-resorts-hotelcasino-back-up/694378/"
        },
        {
            "question": "Did MGM pay ransom?",
            "snippet": "The company has not acknowledged making any ransom payment to the hackers, who have not been identified by the company or law enforcement.",
            "title": "MGM's losses in cyberattack will be insured up to $200 million",
            "link": "https://thenevadaindependent.com/article/mgms-losses-in-cyberattack-will-be-insured-up-to-200-million"
        },
        {
            "question": "How much did Caesars pay hackers?",
            "snippet": "The cybercrime group demanded a $30 million ransom from Caesars, but the company ultimately agreed to pay about half that, sources said. The costs will be partially mitigated by Caesars' cyber insurance policies.\nSep 14, 2023",
            "title": "Caesars paid millions in ransom to cybercrime group prior to MGM hack - CNBC",
            "link": "https://www.cnbc.com/2023/09/14/caesars-paid-millions-in-ransom-to-cybercrime-group-prior-to-mgm-hack.html"
        }
    ],
    "relatedSearches": [
        {
            "query": "Mgm cyber attack what happened"
        },
        {
            "query": "Mgm paid ransom"
        },
        {
            "query": "Mgm ransom amount"
        },
        {
            "query": "Mgm grand cyber attack update"
        },
        {
            "query": "Mgm cyber attack status"
        },
        {
            "query": "Mgm cyber attack reddit"
        },
        {
            "query": "Mgm cyber attack cause"
        },
        {
            "query": "MGM casinos"
        }
    ]
}

keyword = "2 Casino Ransomware Attacks"
prompt = ChatPromptTemplate.from_template("""You will be provided with a block of text, and your task is to extract entity like people, organization, city, company,... that is related to each other and the text block.

<context>
{data}
<context/>  

REMEMBER: Do not Introduce or explain. Return bullet point of Entity List . 
{keyword}
""")
chain = prompt | model
# chain = prompt | model.bind(stop=["\n"])
print(chain.invoke({"data": google_search_data, "keyword": keyword}))

