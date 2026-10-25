#!/usr/bin/env python3
"""
Daily learning point generator (DeepSeek / OpenRouter backends).

Reads index.md, picks fresh angles per active topic, calls an LLM, writes
dated bilingual pages into each topic folder.
"""
import os, re, json, glob, time, urllib.request, urllib.error, sys
from pathlib import Path

VAULT = Path("/workspace/obsidian-learning")
DATE = sys.argv[1] if len(sys.argv) > 1 else "2026-10-26"

# Load env
for line in Path("/workspace/.hermes/.env").read_text().splitlines():
    line = line.strip()
    if line and not line.startswith("#") and "=" in line:
        k, v = line.split("=", 1)
        os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))

DEEPSEEK_KEY = os.environ.get("DEEPSEEK_API_KEY", "")
OPENROUTER_KEY = os.environ.get("OPENROUTER_API_KEY", "")

TOPICS = [
    ("MinIO", "MinIO (S3-compatible object storage)", "minio", 12),
    ("StreamLit", "StreamLit (Python web app framework)", "streamlit", 12),
    ("Radius Server", "Radius Server (Network access control)", "radius-server", 17),
    ("Redis", "Redis (In-memory data store)", "redis", 12),
    ("Vite", "Vite (Next-gen frontend build tool)", "vite", 17),
    ("Meilisearch", "Meilisearch (Lightning fast search engine)", "meilisearch", 17),
    ("Elasticsearch", "Elasticsearch (Distributed search & analytics)", "elasticsearch", 17),
    ("Prisma", "Prisma (Next-gen Node.js ORM)", "prisma", 16),
    ("NestJS", "NestJS (Progressive Node.js framework)", "nestjs", 17),
    ("Flask", "Flask (Python micro web framework)", "flask", 17),
    ("Flutter", "Flutter (Cross-platform UI framework)", "flutter", 12),
    ("Encryption & Decryption", "Encryption & Decryption (Cryptography basics)", "encryption", 12),
    ("Certificate Signing", "Certificate Signing (PKI & TLS certificates)", "cert-signing", 12),
    ("HSM", "HSM (Hardware Security Module)", "hsm", 17),
    ("MCP", "MCP (Model Context Protocol)", "mcp", 19),
]

# Simplified-Chinese characters that must never appear in the zh sections
SIMPLIFIED = set(
    "据网实应该说话语这时间来开关门间问问题实现让给动务员会长级东车马鸟龙义书写"
    "业专严并丧个两严丽举么义乌乐乔习乡书买乱争亚产亲亿仅从仑仓仪们价众优会伤伦"
    "伟传伪佣侠侣侥侦侧侨侩侯俭债倾偿储儿兑兖党兰关兴兹养兽内冈册写军农冯冲决况"
    "冻净凄凉减凑凛几凤凭凯击凿刍划刘则刚创删别刬刭刽刿剀剂剐剑剥剧劝办务劢动"
    "励劳势勋勐勚匀匦匮区医华协单卖卢卤卧卫却厂厅历厉压厌厍厕厢厣厦厨厩厮县参双"
    "发变叙叠叶号叹吗吨听启吴呐呒呓呕呖呗员呙呛呜咏咙咛咝咤咴咸哌响哑哒哓哔哕哗"
    "哙哜哝哟唛唝唠唡唢唣唤唿啧啬啭啮啰啴啸喷喽喾嗫嗳嘘嘤嘱噜嚣团园囱围囵国图圆"
    "圣圹场坂坏块坚坛坜坝坞坟坠垄垅垆垒垦垧垩垫垭垯垱垲垴埘埙埚埝埯堑堕塆墙壮"
    "声壳壶壸处备复够头夸夹夺奁奂奋奖奥妆妇妈妩妪妫姗姜娄娅娆娇娈娱娲娴婳婴婵婶"
    "媪嫒嫔嫱嬷孙学孪宁宝实宠审宪宫宽宾寝对寻导寿将尔尘尧尴尸尽层屃屉届属屡屦屿"
    "岁岂岖岗岘岚岛岭岳岽岿峃峄峡峣峤峥峦崂崃崄崭嵘嵚嵛嵝嵴巅巍巯币帅师帏帐帘帜"
    "带帧帮帱帻帼幂幞干并广庄庆庐庑库应庙庞废庼廪开异弃弑张弥弪弯弹强归当录彟彦"
    "彻径徕御忆忏忧忾怀态怂怃怄怅怆怜总怼怿恋恳恶恸恹恺恻恼恽悦悫悬悯惊惧惨惩惫"
    "惬惭惮惯愍愠愤愦愿慑慭憷懑懒懔戆戋戏戗战戬户扎扑扦执扩扪扫扬扰抚抛抟抠抡抢"
    "护报担拟拢拣拥拦拧拨择挂挚挛挜挝挞挟挠挡挢挣挤挥挦捞损捡换捣据掳掴掷掸掺"
    "掼揸揽揿搀搁搂搅携摄摅摆摇摈摊撄撑撵撷撸撺擞攒敌敛数斋斓斗斩断无旧时旷旸"
    "昙昼昽显晋晒晓晔晕晖暂暧札术朴机杀杂权条来杨杩杰极构枞枢枣枥枧枨枪枫枭柜柠"
    "柽标栈栉栊栋栌栎栏树栖样栾桊桠桡桢档桤桥桦桧桨桩梦梼梾检棂椁椟椠椤椭楼榄"
    "榇榈榉槚槛槟槠横樯樱橥橱橹橼檐檩欢欤欧歼殁殇残殒殓殚殡殴毁毂毕毡毵氅氇气氢"
    "氩氲汇汉污汤汹沟没沣沤沥沦沧沨沩沪沵泞泪泶泷泸泺泻泼泽泾洁洒洼浃浅浆浇浈浉"
    "浊测浍济浏浐浑浒浓浔浕涂涌涛涝涞涟涠涡涢涣涤润涧涨涩淀渊渌渍渎渐渑渔渖渗"
    "温游湾湿溃溅溆溇滗滚滞滟滠满滢滤滥滦滨滩滪漤潆潇潋潍潜潴澜濑濒灏灭灯灵灾灿"
    "炀炉炖炜炝点炼炽烁烂烃烛烟烦烧烨烩烫烬热焕焖焘煅煳熘爱爷牍牦牵牺犊犟状犷犸犹"
    "狈狍狝狞独狭狮狯狰狱狲猃猎猕猡猪猫猬献獭玑玙玚玛玮环现玱玺珉珏珐珑珰珲琎琏"
    "琐琼瑶瑷璇璎瓒瓮瓯电画畅畲畴疖疗疟疠疡疬疮疯疱疴痈痉痒痖痨痪痫痴瘅瘆瘗瘘"
    "瘪瘫瘾瘿癞癣癫癯皑皱皲盏盐监盖盗盘眍眦眬着睁睐睑瞒瞩矫矶矾矿砀码砖砗砚砜砺砻"
    "砾础硁硕硖硗硙硚确硷碍碛碜碱碹磙礼祎祢祯祷祸禀禄禅离秃秆种积称秽秾稆税稣稳"
    "穑穷窃窍窎窑窜窝窥窦窭竖竞笃笋笔笕笺笼笾筑筚筛筜筝筹签简箓箦箧箨箩箪箫篑篓"
    "篮篱簖籁籴类籼粜粝粤粪粮糁糇紧絷纟纠纡红纣纤纥约级纨纩纪纫纬纭纯纰纱纲纳"
    "纵纶纷纸纹纺纻纼纽纾线绀绁绂练组绅细织终绉绊绋绌绍绎经绐绑绒结绔绕绖绗绘给"
    "绚绛络绝绞统绠绡绢绣绤绥绦继绨绩绪绫绬续绮绯绰绱绲绳维绵绶绷绸绹绺绻综绽"
    "绾绿缀缁缂缃缄缅缆缇缈缉缊缋缌缍缎缏缑缒缓缔缕编缗缘缙缚缛缜缝缞缟缠缡缢缣"
    "缤缥缦缧缨缩缪缫缬缭缮缯缰缱缲缳缴缵罂网罗罚罢罴羁羟羡翘翙翚耢耧耸耻聂聋职"
    "聍联聩聪肃肠肤肷肾肿胀胁胆胜胧胨胪胫胶脉脍脏脐脑脓脔脚脱脶脸腊腌腘腭腻腼腾"
    "膑臜舆舣舰舱舻艰艳艹艺节芈芗芜芦苁苇苈苋苌苍苎苏苘苹茎茏茑茔茕茧荆荐荙荚"
    "荛荜荞荟荠荡荣荤荥荦荧荨荩荪荫荬荭荮药莅莜莱莲莳莴莶获莸莹莺莼萚萝萤营萦萧"
    "萨葱蒇蒉蒋蒌蓝蓟蓠蓣蓥蓦蔷蔹蔺蔼蕲蕴薮藓藬蘖虏虑虚虫虬虮虽虾虿蚀蚁蚂蚕蚝蚬"
    "蛊蛎蛏蛮蛰蛱蛲蛳蛴蜕蜗蜡蝇蝈蝉蝎蝼蝾螀螨蟏衅衔补衬衮袄袅袆袜袭袯装裆裈裢裣"
    "裤裥褛褴襁襕见观觃规觅视觇览觉觊觋觌觍觎觏觐觑觞触觯詟誉誊讠计订讣认讥讦"
    "讧讨让讪讫训议讯记讱讲讳讴讵讶讷许讹论讻讼讽设访诀证诂诃评诅识诇诈诉诊诋诌"
    "词诎诏诐译诒诓诔试诖诗诘诙诚诛诜话诞诟诠诡询诣诤该详诧诨诩诪诫诬语诮误诰"
    "诱诲诳说诵诶请诸诹诺读诼诽课诿谀谁调谄谅谆谇谈谊谋谌谍谎谏谐谑谒谓谔谕谖谗"
    "谘谙谚谛谜谝谞谟谠谡谢谣谤谥谦谧谨谩谪谫谬谭谮谯谰谱谲谳谴谵谶谷豮贝贞负贠"
    "贡财责贤败账货质贩贪贫贬购贮贯贰贱贲贳贴贵贶贷贸费贺贻贼贽贾贿赀赁赂赃资赅"
    "赆赇赈赉赊赋赌赍赎赏赐赑赒赓赔赕赖赗赘赙赚赛赜赝赞赟赠赡赢赣赪赵赶趋趱趸跃跄"
    "跖跞践跶跷跸跹跻踊踌踪踬踯蹑蹒蹰蹿躏躜躯车轧轨轩轪轫转轭轮软轰轱轲轳轴轵轶"
    "轷轸轹轺轻轼载轾轿辀辁辂较辄辅辆辇辈辉辊辋辌辍辎辏辐辑辒输辔辕辖辗辘辙辚辞"
    "辩辫边辽达迁过迈运还这进远违连迟迩迳迹适选逊递逦逻遗遥邓邝邬邮邹邺邻郁郄郏"
    "郐郑郓郦郧郸酝酦酱酿释里鉅鉴銮錾钅钆钇针钉钊钋钌钍钎钏钐钑钒钓钔钕钖钗钘钙"
    "钚钛钜钝钞钟钠钡钢钣钤钥钦钧钨钩钪钫钬钭钮钯钰钱钲钳钴钵钶钷钸钹钺钻钼钽钾"
    "钿铀铁铂铃铄铅铆铈铉铊铋铌铍铎铏铐铑铒铕铗铘铙铚铛铜铝铞铟铠铡铢铣铤铥铦铧铨"
    "铩铪铫铬铭铮铯铰铱铲铳铴铵银铷铸铹铺铻铼铽链铿销锁锂锃锄锅锆锇锈锉锊锋锌"
    "锍锎锏锐锑锒锓锔锕锖锗错锚锛锜锞锟锠锡锢锣锤锥锦锨锩锪锫锬锭键锯锰锱锲锴锶"
    "锷锸锹锺锻锼锾锿镀镁镂镃镆镇镈镉镊镌镍镎镏镐镑镒镓镔镖镗镘镚镛镜镝镞镟镠镡"
    "镢镣镤镥镦镧镨镩镪镫镬镭镮镯镰镱镲镳镴镶长门闩闪闫闬闭问闯闰闱闲闳间闵闶闷闸"
    "闹闺闻闼闽闾闿阀阁阂阃阄阅阆阇阈阉阊阋阌阍阎阏阐阑阒阓阔阕阖阗阘阙阚阛队阳阴"
    "阵阶际陆陇陈陉陕陧陨险随隐隶隽难雏雠雳雾霁霉霭靓静靥鞑鞒鞯鞴韦韧韩韪韫韬韵页"
    "顶顷顸项顺须顼顽顾顿颀颁颂颃预颅领颇颈颉颊颋颌颍颎颏颐频颒颓颔颕颖颗题颙"
    "颚颛颜额颞颟颠颡颢颤颥颦颧风飏飐飑飒飓飕飘飙飚飞飨餍饤饥饦饧饨饩饪饫饬饭饮"
    "饯饰饱饲饳饴饵饶饷饸饹饺饻饼饽饾饿馀馁馂馃馄馅馆馇馈馉馊馋馌馍馎馏馐馑馒"
    "馓馔馕马驭驮驯驰驱驲驳驴驵驶驷驸驹驺驻驼驽驾驿骀骁骂骃骄骅骆骇骈骉骊骋验骍"
    "骎骏骐骑骒骓骔骕骖骗骘骙骚骛骜骝骞骟骠骡骢骣骤骥骦骧髅髋髌鬓魇魉鱼鱽鱾鱿鲀"
    "鲁鲂鲃鲅鲆鲇鲈鲉鲊鲋鲌鲍鲎鲏鲐鲑鲒鲔鲕鲖鲗鲘鲙鲚鲛鲜鲝鲞鲟鲠鲡鲢鲣鲤鲥鲦鲧鲨"
    "鲩鲪鲫鲬鲭鲮鲯鲰鲱鲲鲳鲴鲵鲶鲷鲸鲹鲺鲻鲼鲽鲾鲿鳀鳁鳂鳃鳄鳅鳆鳇鳈鳉鳊鳋鳌"
    "鳍鳎鳏鳐鳑鳒鳓鳔鳕鳖鳗鳘鳙鳚鳛鳜鳝鳞鳟鳠鳡鳢鳣鸟鸠鸡鸢鸣鸤鸥鸦鸧鸨鸩鸪鸫鸬"
    "鸭鸮鸯鸰鸱鸲鸳鸴鸵鸶鸷鸸鸹鸺鸻鸼鸽鸾鸿鹀鹁鹂鹃鹄鹅鹆鹇鹈鹉鹊鹋鹌鹍鹎鹏鹐鹑鹒鹓"
    "鹔鹕鹖鹗鹘鹙鹚鹛鹜鹝鹞鹟鹠鹡鹢鹣鹤鹥鹦鹧鹨鹩鹪鹫鹬鹭鹯鹰鹱鹲鹳鹴鹾麦麸黄黉黡黩黪黾"
    "鼋鼌鼍鼗鼹齄齐齑齿龀龁龂龃龄龅龆龇龈龉龊龋龌龙龚龛龟"
)

SYSTEM = """You are a patient teacher writing an ELI5-style learning page for a curious university undergraduate.
Output STRICT JSON only (no markdown fences, no prose outside JSON): a JSON array of objects.

Each object: {"title": "<short English heading, no markdown>", "en": "<3-5 developed paragraphs>", "zh": "<full Traditional Chinese translation of en, same length>", "takeaway": "<one sentence written in ENGLISH>", "related": ["concept A", "concept B"]}

HARD RULES:
- "zh" MUST be Traditional Chinese (繁體中文, Hong Kong style). NEVER Simplified characters (e.g. use 據/網/實/應該, never 据/网/实/应该). Use 「」 or 「」 style quotes sparingly.
- "en" and "zh" must be substantial: roughly 5 minutes of reading each, 3-5 real paragraphs with concrete examples, analogies, and technical detail. Explain jargon on first use.
- Cover DISTINCT angles from each other and from the already-covered headings provided.
- Accuracy is critical: only state technical facts you are confident about (commands, flags, API routes, version-specific features, RFC numbers). If unsure of a specific detail, describe the concept generally instead of inventing specifics.
- Public and neutral: no personal names, no mention of any person, user, assistant, or conversation.
- "title" must not contain markdown syntax.
- "related": exactly 2 concepts.
"""

USER = """Topic: {topic}

Already covered in this vault (do NOT repeat these angles):
{covered}

Generate exactly {n} NEW learning points for this topic, each covering a fresh, distinct angle. Make them deep and genuinely educational.

Reply with JSON array only."""

MERMAID_HINT = """Also make sure the content describes processes where a simple flow diagram would help; the writer will add a Mermaid diagram separately."""


def call_llm(prompt, system, model="deepseek-chat", provider="deepseek", retries=3):
    if provider == "deepseek":
        url = "https://api.deepseek.com/chat/completions"
        key = DEEPSEEK_KEY
        payload_model = model
    else:
        url = "https://openrouter.ai/api/v1/chat/completions"
        key = OPENROUTER_KEY
        payload_model = model
    body = {
        "model": payload_model,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": prompt},
        ],
        "max_tokens": 12000,
        "temperature": 0.7,
    }
    last = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(
                url, data=json.dumps(body).encode(),
                headers={"Content-Type": "application/json", "Authorization": f"Bearer {key}"},
            )
            with urllib.request.urlopen(req, timeout=300) as r:
                data = json.loads(r.read().decode())
            return data["choices"][0]["message"]["content"]
        except Exception as e:
            last = e
            print(f"    attempt {attempt+1} failed: {e}", flush=True)
            time.sleep(5 * (attempt + 1))
    raise RuntimeError(f"LLM failed: {last}")


def extract_json(text):
    t = text.strip()
    t = re.sub(r"^```(?:json)?\s*", "", t)
    t = re.sub(r"\s*```$", "", t)
    start = t.find("[")
    end = t.rfind("]")
    if start == -1 or end == -1:
        raise ValueError("no JSON array found")
    return json.loads(t[start:end + 1])


def existing_headings(slug):
    hs = []
    for f in sorted(glob.glob(str(VAULT / slug / "*.md"))):
        for line in open(f, encoding="utf-8"):
            s = line.strip()
            if s.startswith("# ") and len(s) < 130:
                hs.append(s[2:])
    return hs


def slugify_topic(name):
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def mermaid_for(topic, title, en):
    """Generate a small mermaid flowchart describing the concept."""
    p = call_llm(
        f"Topic: {topic}\nLearning point title: {title}\n\nSummary of the point:\n{en[:1800]}\n\n"
        "Write ONE Mermaid flowchart (type `flowchart TD`) that visualises the main mechanism described.\n"
        "HARD RULES: node labels must be plain ASCII words inside [ ] only — no parentheses, no slashes, no quotes, no special characters. "
        "Use at most 8 nodes. Edge labels only if simple single words. Output the mermaid code ONLY, no fences, no explanation.",
        "You output only valid Mermaid flowchart code. No prose, no markdown fences.",
        model="deepseek-chat", provider="deepseek", retries=2)
    code = re.sub(r"^```(?:mermaid)?\s*", "", p.strip())
    code = re.sub(r"\s*```$", "", code).strip()
    # sanitize labels
    def fix(m):
        label = m.group(1)
        label = re.sub(r"[^\w \-\.:/]", "", label)
        label = label.replace("[", "").replace("]", "").replace("/", " ").replace("(", "").replace(")", "")
        label = re.sub(r"\s+", " ", label).strip()
        return "[" + label + "]"
    code = re.sub(r"\[([^\]]*)\]", fix, code)
    code = re.sub(r"\{([^\}]*)\}", lambda m: "{" + re.sub(r"[^\w\- ]", "", m.group(1)) + "}", code)
    if not code.startswith("flowchart"):
        code = "flowchart TD\n    A[Concept] --> B[Detail]"
    return code


def write_page(slug, short, num, obj, date):
    path = VAULT / slug / f"{date} - {short} - Learning Point {num}.md"
    lines = [
        "---",
        f'title: "{date} - {short} - Learning Point {num}"',
        "tags:",
        "  - learning",
        f"  - {slug}",
        f"created: {date}",
        "---",
        "",
        f"# {obj['title']}",
        "",
        "## English",
        "",
        obj["en"].strip(),
        "",
        "## 中文",
        "",
        obj["zh"].strip(),
        "",
        "## Key Takeaway",
        "",
        obj["takeaway"].strip(),
        "",
        "## Related Concepts",
    ]
    for c in obj.get("related", [])[:2]:
        lines.append(f"- {c}")
    lines.append("")
    lines.append("## Diagram")
    lines.append("```mermaid")
    lines.append(obj.get("mermaid", "flowchart TD\n    A[Concept] --> B[Detail]"))
    lines.append("```")
    lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def simplified_hits(text):
    """Return characters that opencc would convert (i.e. simplified forms present)."""
    try:
        from opencc import OpenCC
        cc = OpenCC("s2t")
    except Exception:
        return set()
    hits = set()
    for ch in text:
        if "一" <= ch <= "鿿" and cc.convert(ch) != ch:
            hits.add(ch)
    return hits


def to_traditional(text):
    """Convert simplified Chinese to Traditional Chinese (HK variant) using opencc."""
    try:
        from opencc import OpenCC
        cc = OpenCC("s2twp")
        return cc.convert(text)
    except Exception:
        return text


def fix_simplified(text):
    """Convert any simplified Chinese into traditional Chinese via opencc."""
    bad = sorted(simplified_hits(text))
    if not bad:
        return text, []
    return to_traditional(text), bad


def main():
    only = sys.argv[2].split(",") if len(sys.argv) > 2 else None
    created, errors = 0, []
    for short, topic, slug, start_num in TOPICS:
        if only and slug not in only:
            continue
        folder = VAULT / slug
        folder.mkdir(parents=True, exist_ok=True)
        covered = existing_headings(slug)
        print(f"[{topic}] covered headings: {len(covered)}", flush=True)
        try:
            out = call_llm(
                USER.format(topic=topic, covered="\n".join(f"- {h}" for h in covered) or "(none)", n=3),
                SYSTEM)
            pts = extract_json(out)
            if len(pts) < 3:
                raise ValueError(f"only {len(pts)} points returned")
            for i, obj in enumerate(pts[:3]):
                num = start_num + i
                fixed, bad = fix_simplified(obj["zh"])
                if bad:
                    print(f"    fixed simplified chars {bad}", flush=True)
                    obj["zh"] = fixed
                obj["mermaid"] = mermaid_for(topic, obj["title"], obj["en"])
                p = write_page(slug, short, num, obj, DATE)
                print(f"  wrote {p.name}", flush=True)
                created += 1
                time.sleep(1)
        except Exception as e:
            errors.append(f"{topic}: {e}")
            print(f"  ERROR {topic}: {e}", flush=True)
    print(f"\nDONE created={created} errors={len(errors)}")
    for e in errors:
        print(" -", e)


if __name__ == "__main__":
    main()
