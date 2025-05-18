# 假新闻网站聚类数据，直接以 Python 列表形式定义
def get_fake_news_web():
    fake_news_clusters = [
        ["neonnettle.com", "newsthud.com", "newspushed.com"],
        ["vaccineimpact.com", "freecoconutrecipes.com", "medicalkidnap.com", "healthytraditions.com", "coconutoil.com", "healthimpactnews.com"],
        ["thetruthaboutvaccines.com", "thetruthaboutcancer.com"],
        ["jpands.org", "aapsonline.org"],
        ["arkencounter.com", "answersingenesis.org", "creationmuseum.org"],
        ["newscorpse.com", "www.blazingcatfur.ca"],
        ["www.meforum.org", "www.futureofcapitalism.com", "www.danielpipes.org"],
        ["thinkamericana.com", "dailypoliticalnewswire.com"],
        ["republicaninformer.com", "wethepeopledaily.com", "teaparty.org", "justpatriots.com", "www.teaparty.org", "sonsof1776.com", "thelibertyrevolution.com", "nationalinsiders.com", "thebeardedpatriot.com", "patrioticpost.com", "libertybell.com"],
        ["www.pop.org", "overpopulationisamyth.com"],
        ["www.veteranstodayarchives.com", "www.veteranstoday.com"],
        ["tv.infowars.com", "www.infowarsshop.com", "www.prisonplanet.com"],
        ["sputniknews.com", "snanews.de", "sputniknews.gr", "sputniknews.cn"],
        ["www.whitsundaytimes.com.au", "www.adelaidenow.com.au", "www.townsvillebulletin.com.au", "www.ntnews.com.au", "www.themercury.com.au", "www.southburnetttimes.com.au", "www.tweeddailynews.com.au", "www.delicious.com.au", "www.cqnews.com.au", "www.heraldsun.com.au", "www.couriermail.com.au", "www.news-mail.com.au", "www.sunshinecoastdaily.com.au", "www.geelongadvertiser.com.au", "www.bestrecipes.com.au", "www.gladstoneobserver.com.au", "www.themorningbulletin.com.au", "www.frasercoastchronicle.com.au", "www.dailytelegraph.com.au", "www.noosanews.com.au", "www.warwickdailynews.com.au", "www.escape.com.au", "www.seniorsnews.com.au", "www.gq.com.au", "www.weeklytimesnow.com.au", "www.ballinaadvocate.com.au", "www.goldcoastbulletin.com.au", "www.news.com.au", "www.gympietimes.com.au", "www.dailymercury.com.au", "www.gattonstar.com.au", "www.thechronicle.com.au", "www.stanthorpeborderpost.com.au", "www.northernstar.com.au", "www.bodyandsoul.com.au", "www.vogue.com.au", "www.kidspot.com.au", "www.chinchillanews.com.au", "www.byronnews.com.au", "www.dalbyherald.com.au", "www.taste.com.au", "www.qt.com.au", "www.cairnspost.com.au", "www.theaustralian.com.au"],
        ["www.americanthinker.com", "medcitynews.com", "www.climatedepot.com", "deepleftfield.info"],
        ["www.elijahlist.com", "breakingchristiannews.com"],
        ["www.nvic.org", "thevaccinereaction.org"],
        ["www.fairus.org", "www.immigrationreform.com"],
        ["www.12minutos.com", "www.react365.com"],
        ["www.preaching.com", "redstate.com", "www.biblestudytools.com", "larryelder.com", "www.godtube.com", "www.crosswalk.com", "srnnews.com", "www.historyonthenet.com", "www.allcreated.com", "twitchy.com", "bearingarms.com", "www.crosscards.com", "pjmedia.com", "www.christianheadlines.com", "hughhewitt.com", "www.biblegateway.com", "www.bibliavida.com", "www.praywithme.com", "mikeonline.com", "www.godvine.com", "www.churchangel.com", "www.christianity.com", "www.sebgorka.com", "www.ibelieve.com", "hotair.com", "townhall.com", "dennisprager.com", "www.teachertube.com", "www.oneplace.com", "saleminteractivemedia.com", "ccmmagazine.com", "am870theanswer.com", "singingnews.com", "www.christianradio.com", "www.elsitiocristiano.com", "am970theanswer.com", "710knus.com", "www.christianjobs.com", "kkla.com", "www.churchstaffing.com", "930amtheanswer.com", "www.godupdates.com", "taylorvilledailynews.com", "salemsurround.com", "www.lightsource.com", "www.salemwebnetwork.com", "www.sermonsearch.com", "preferences.salemwebnetwork.com", "www.salemallpass.com"],
        ["redstatewatcher.com", "redstateobserver.com"],
        ["english.pravda.ru", "www.politonline.ru", "www.moneytimes.ru", "www.pravda.ru", "www.bigness.ru", "www.georgiatimes.info"],
        ["professorwatchlist.org", "www.tpusa.com"],
        ["dailyheadlines.net", "threepercenternation.com"],
        ["www.charismanews.com", "ministrytodaymag.com", "charismamag.com"],
        ["www.activistpost.com", "www.naturalblaze.com"],
        ["www.globalwarming.org", "cei.org"],
        ["sustainablepulse.com", "detoxproject.org"],
        ["www.returnofkings.com", "www.rooshv.com"],
        ["metro.co.uk", "www.dailymail.co.uk"],
        ["www.antiwar.com", "ballot-access.org", "antiwar.com", "www.lewrockwell.com"],
        ["www.rightjournalism.com", "defiantamerica.com", "conservativeus.com", "www.usasupreme.com", "redstatenation.com"],
        ["www.frontpagemag.com", "www.jihadwatch.org", "frontpagemag.com"],
        ["www.asia-pacificresearch.com", "www.mondialisation.ca", "www.globalresearch.ca"],
        ["www.henrymakow.com", "www.savethemales.ca"],
        ["www.eagnews.org", "www.theamericanmirror.com"],
        ["en.newsner.com", "www.thelaughclub.net"],
        ["persopo.com", "conservativedailypost.com", "www.floridaresidentsdirectory.com"],
        ["dissentfromdarwin.org", "intelligentdesign.org", "mindmatters.ai", "www.discovery.org", "evolutionnews.org"],
        ["americasfreedomfighters.com", "rightwingtribune.com", "breakingfirst.com"],
        ["empirenews.net", "en-volve.com"],
        ["collegecandy.com", "bustedcoverage.com", "coed.com"],
        ["www.conservativeglobe.com", "www.americanlibertyemail.com"],
        ["freedomforceinternational.org", "needtoknow.news"],
        ["americanpeopledaily.com", "newssloth.com"],
        ["www.newsmaxtv.com", "www.newsmax.com", "shop.newsmax.com"],
        ["nypost.com", "pagesix.com", "decider.com", "www.weaselzippers.us"],
        ["theeconomiccollapseblog.com", "endoftheamericandream.com", "themostimportantnews.com"],
        ["www.rt.com", "rtd.rt.com"],
        ["www.healthyfoodhouse.com", "thetruereporter.com"],
        ["detoxproject.org", "sustainablepulse.com"],
        ["curiousmindmagazine.com", "thepowerofsilence.co"],
        ["thenewamerican.com", "jbs.org"],
        ["dissentfromdarwin.org", "evolutionnews.org", "intelligentdesign.org", "mindmatters.ai", "www.discovery.org"],
        ["power1051.iheart.com", "ktrh.iheart.com", "kiss108.iheart.com", "933flz.iheart.com", "z100.iheart.com", "wrko.iheart.com", "wtam.iheart.com", "www.at40.com", "kiisfm.iheart.com", "whp580.iheart.com", "710wor.iheart.com", "kfyi.iheart.com", "onairwithryan.iheart.com", "rock103.iheart.com", "q1043.iheart.com", "wflanews.iheart.com", "kfiam640.iheart.com", "www.brookeandjeffrey.com", "dc101.iheart.com", "koanewsradio.iheart.com", "700wlw.iheart.com", "elvisduran.iheart.com", "hot995.iheart.com", "kfan.iheart.com", "ktu.iheart.com", "woai.iheart.com", "www.coasttocoastam.com", "www.iheart.com"],
        ["www.projectveritas.com", "i2i.org", "blexitfoundation.org"],
        ["adfmedia.org", "adflegal.org"],
        ["djhjmedia.com", "davidharrisjr.com"],
        ["conservativefiringline.com", "thebullelephant.com"],
        ["hsionline.com", "healthiertalk.com", "allianceforadvancedhealth.com"],
        ["www.pluggedin.com", "www.focusonthefamily.com"],
        ["www.realmilk.com", "www.westonaprice.org"],
        ["offgridsurvival.com", "networkinvegas.com"],
        ["linkiest.com", "rightwingnews.com"],
        ["www.frcaction.org", "frcblog.com", "frc.org"],
        ["occupydemocrats.com", "washingtonpress.com"],
        ["comicallyincorrect.com", "clashdaily.com"],
        ["iceagenow.com", "www.iceagenow.info"],
        ["dcdirtylaundry.com", "lidblog.com", "bb4sp.com"],
        ["transnational.org", "rumormillnews.com"],
        ["lawandcrime.com", "www.mediaite.com", "breaking911.com"],
        ["dailycaller.com", "checkyourfact.com", "smokeroom.com"],
        ["www.mrc.org", "newsbusters.org", "cnsnews.com", "www.mrctv.org"]
    ]

    # 示例用途：输出总聚类数和其中一个聚类内容
    #print(f"总共有 {len(fake_news_clusters)} 个假新闻站点聚类")
    #print("第一个聚类的站点有：", fake_news_clusters[0])




    # 原始聚类数据（请确保你已定义 fake_news_clusters）
    fake_news_domains_raw=[domain for cluster in fake_news_clusters for domain in cluster]
    fake_news_domains=set(domain.replace("www","") for domain in fake_news_domains_raw)
    #print(fake_news_domains)
    #print(len(fake_news_domains))
    return fake_news_domains
if __name__=="__main__":
    get_fake_news_web()
