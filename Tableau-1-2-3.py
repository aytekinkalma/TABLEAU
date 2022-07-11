# TABLEAU
# NOT: Alttaki ilk bölümlerde ### ile işaretli yerler özet kısım. Sadece buralara da göz atılabilir tercihen

#%% TABLEAU - 1
#####################
# Tableau
    # Tableau, verilerinizi görsel olarak analiz etmek için güçlü bir İş Zekası (BI) aracıdır
    # BI toolların amacı veriyi görselleştirerek daha anlamlı insight lar çıkartıp karşı tarafa istediğimiz mesajı vermek
    ### BI tools: Microsoft Power BI, Data Studio, Looker, Qlik,. Tableau öğrendikten sonra bunları rahat bir şekilde öğreneceksiniz
    ### Sektör liderleri: 1.Microsoft Power BI, 2.Tableau , 3.Qlik
    
#####################    
# Iş Zekası Nedir?
    # Geleneksel İş Zekası ilk olarak 1960'larda kuruluşlar arasında bilgi paylaşım sistemi olarak ortaya çıktı. 
    # .. 1980'lerde, BT'ye bağlı hizmet çözümleriyle BI ekiplerinden belirli bir teklif haline gelmeden önce, karar verme ve veri 
    # .. içgörülerini dönüştürmeye yönelik bilgisayar modelleriyle birlikte daha da geliştirildi.
    ### Neredeyse bütün işletmeler kullanıyor
    # Bir şirketiniz olsun. Satış yapıyorsunuz. Bu satışları işlem kaydı olarak excelde, db de, AWS de vs tutuyorsunuz
    # Bu verileri sonra periyodik olarak gözlemleyip analiz yapmamız gerekiyor. BI tool lar burada devreye giriyor
    # Kullandığımız tablo ile BI tool arasında connection oluşturuyoruz insightlar çıkartıyoruz.
    # Bu insigtlar, hedefler olabilir. Şu kadar yüzdenin üstünde satışı geçtik mi diye görsel/view hazırlayabiliriz
    ### Python ve SQL nerede işe yarayacak? Bu bağlantı aşamasında köprü olarak kullanacağız
    ### Tableau daki verisetinin temiz olması gerekiyor görselleri oluşturabilmek için.
    # Sonra bu oluşturduğum insight ları paylaşmam gerekiyor. Bunu yöneticiye götürebiliriz
    # Dashboard lar oluşturabiliriz. Karşı taraf üzerinde oynamalar yapabilir
    # İçerisinde yer aldığınız şirkete göre paylaşacağınız kişiler değişebilir. Müşteri, başka şirket, patronunuz,
    # .. karar vericiler(şirketteki diğer departmanlar) vs. Onlar kendilerine göre bu insighları kullanacak.    
    ### Geçtiğimiz yıllarda iş zekası, performansı iyileştirmeye yardımcı olmak için daha fazla süreç ve aktivite 
    ### .. içerecek şekilde gelişti. Bu süreçler şunları içeriyor:
        # Data mining
        # Reporting
        # Performance metrics and benchmarking
        # Descriptive analytics
        # Querying
        # Statistical analysis
        # Data visualization
        # Visual analysis
        # Data preparation
   ### BI döngüsü : Verileri toplama --> Verileri temizleme ve BI tool a aktarma --> dashboardlar/insightlar çıkartma --> 
   ### .. --> Share(karar vericilerle) --> Karar verme sonucunda yeni kararlar alındı, indirimler, satışlar yapıldı vs
   ### .. sonra döngü tekrar başa satıyor --> --> (yeni) verileri toplama --> ...
        
#####################
# Neden Tableau'yu öğreniyoruz?
    ### Tableau'da düşünce hızında sürükle ve bırak özelliği ile kolayca grafikler oluşturabilirsiniz
    # Tableau ile verilerinizi keşfeder, analiz eder, ardından bulgularınızı sunar ve meslektaşlarınız, 
    # .. ortaklarınız veya müşterilerinizle paylaşırsınız. Herkes sürükle ve bırak yöntemiyle verileri analiz edebilir. 
    # .. Verilerinizi dakikalar içinde bağlayabilir ve görselleştirebilirsiniz. Yüksek düzeyde etkileşimli gösterge 
    # .. tabloları (birkaç grafikten oluşan) oluşturabilir ve daha fazla bilgi edinmek için bunlarla etkileşime girebilirsiniz
    ### Tableau, analiz sürecini basitleştirmek ve hızlandırmak için daha geniş Yapay Zeka (AI) şemsiyesi içinde Doğal Dil 
    ### .. İşleme (NLP) ve Makine Öğrenimi gibi yeni ve gelişmekte olan teknolojilerden yararlanıyor. Bu aynı zamanda BI'da
    ### .. "Augmented analytics" olarak adlandırılan eğilimi de desteklemektedir. Gartner'a göre Augmented analytics tanımı:
        ### Makine öğrenimi (ML) ve yapay zeka (AI) destekli veri hazırlama, içgörü(insight) oluşturma(çıkarma) ve açıklama -
        ### .. Iş insanlarının ve analistlerin verileri nasıl keşfettiğini ve analiz ettiğini artırmak - 
        ### .. Hızla rekabetçi farklılaşmanın temel kaynakları haline geliyor. Bu nedenle satıcılar için temel bir yatırım.

#####################
# Tableau Products
# Tableau firmasının sahip olduğu dört ana ürün bulunmaktadır. Bunlar:
    # Tableau Desktop
    # Tableau Prep Builder
    # Tableau Server
    # Tableau Online

#####################
# Tableau Desktop
    # Tableau Desktop, görsel analitik gerçekleştirmek için çeşitli araçlara sahiptir. Tableau Desktop'ta grafikler, haritalar, 
    # .. panolar ve hikayeler oluşturabilirsiniz. Tableau Desktop'ın iki versiyonu vardır: biri Tableau Desktop Professional, diğeri 
    # .. Tableau Desktop Public. Tableau Desktop Professional'ı kullanmak için bir lisans anahtarınız olması gerekir, bu da onun 
    # .. ücretli versiyonu anlamına gelir. Tableau Desktop Public ücretsiz bir sürümüdür. Ancak Tableau Desktop Professional ile 
    # .. karşılaştırıldığında bazı sınırlı yetenekleri vardır. Kurs boyunca Tableau Desktop Professional kullanacağız.

    # Tableau Desktop professional
        # Çalışmaları kendi bilgisayarınıza kaydedebilirsiniz
        # Satın aldığınızda bir "key" i 2 farklı hesapta kullanabilirsiniz
    # Tableau Desktop Public
        # Çalışmaları kendi bilgisayarınıza kaydedemiyorsunuz
        # Metodlar çok fazla değişiklik göstermiyor
        
#####################
# Tableau Prep Builder
    # Verilerinizi hazırlamayı kolay ve sezgisel hale getirmek için tasarlanmış Tableau ürün paketindeki bir araçtır. 
    # Tableau Desktop'ta analiz için verilerinizi birleştirmek, şekillendirmek ve temizlemek için Tableau Prep Builder kullanılabilir.
    # .. Ancak çok gelişmiş bir tool değildir. Hala geliştiriliyor.
    
#####################
# Tableau Server
    # Hazırladığınız dashboardları paylaşma aşamasında kendi şirketinizin server ını, bulut sistemini vs kullanabiliriz
    # Tableau Server, Tableau Desktop'ta oluşturulan görselleştirmelerinizi organizasyonunuz ile paylaşmak için kullanılır

#####################
# Tableau Online
    # Hazırladığınız dashboardları bulutta paylaşma aşamasında tableau sitesini kullanabilirsiniz
    # Tableau Online, bulutta self servis analitik olarak adlandırılır. Bir sunucuyu yönetmeniz gerekmez. 
    # Görselleştirmelerinizi kolayca oluşturabilir, yayınlayabilir ve meslektaşlarınız veya müşterilerinizle paylaşabilirsiniz.

#####################
# Tableauda Veriseti Tanımı
    # Tableau bağlamında, bir veri seti (bazen veri kaynağı veya veritabanı olarak adlandırılır), görselleştirmeler oluşturmak için 
    # .. kullanılan verileri içerir. Tableau'da gördüğünüz çizgi grafik, çubuk grafik gibi her grafiğin, verileri besleyen bağlantılı
    # .. bir veritabanı veya spreadsheet vardır.

#####################
# Veri Kaynaklarının Türleri
    # Tableau'da bağlandığınız dört farklı veri kaynağı türü vardır:
        # Spreadsheets         : Microsoft Excel, Google sheets, Csv, Text file
        # Relational databases : MySQL, MS SQL Server, Postgresql, etc.
        # Cloud data           : Amazon Web Services, Microsoft Azure, Google Cloud 
        # Others               : Spatial files for mapping, Statistical files, Pdf files
            # Tableau'nun bağlanabileceği veri kaynaklarının tam listesi;
            # https://help.tableau.com/current/pro/desktop/en-us/exampleconnections_overview.htm

#####################
# Data Pane
    # Tableau'da veri kaynağını bağladığınızda, veri kümesindeki alanlara otomatik olarak bir "role" ve bir "type" atanı
        # Role : Bir alana(Field) "Dimension role" ya da  "Measure role"  atanabilir
            # Alan(Field): A field (diğer dıyla, sütun ya da özellik(attribute)) , bir kaydın (veya satırın) bir parçasıdır ve
            # .. kaydın konusu için tek bir veri parçası içerir
            # Aşağıda employees tablosuna bakalım. Genelde emp_id, first_name, last_name, salary, etc., bunlara sütun deriz.
            # .. Ama artık, Bunlara alan(field) diyeceğiz
"""
            emp_id	first_name	last_name	salary	job_title	          gender	hire_date
            17679	Robert	     Gilmore	110000	Operations Director	  Male	    2018-09-04
            26650	Elvis	      Ritter	86000	Sales Manager	      Male	    2017-11-14
            30840	David	      Barrow	85000	Data Scientist	      Male	    2019-12-12
            """  
            # Kategorik verilere "dimension", Nümerik verilere "Measures" diyebiliyoruz. Diğer bir tanımlama ile,
            # Tableau, alanları nicel veya nitel olarak ele alır. Nicel alanlara "Measurements" , nitel alanlara "Dimensions" denir. 
            # "Dimensions" adları, tarihleri, unvanları veya coğrafi verileri vb. içerir. "Measurements" maaş, satış, kâr vb. gibi
            # .. ölçebileceğiniz nümeric değerleri içerir. Bir veri setine bağlandığınızda, Tableau alanları, 
            # .. otomatik olarak Dimensions ve Measurements atar.
            # Veri setimizin nitel alanları (Dimensions) üst kısımda, nicel alanlar (Measurements) alt kısımda yer almaktadır.
            # "Measurements" ve "Dimensions", Tableau çizelgelerinin yapı taşlarıdır.
            # An example of dimension is "job title". An examples of measure is "temperature". 
       # Data Types: Alanın veri türü, örneğin, string, integer, date vs. Tableau, türü uygun şekilde atamadıysa, bunu değiştirebiliriz
           # String --> Abc , Date--> (takvim simgesi) , datetime --> (takvim ve saat simgesi), 
           # .. Numeric(Whole,Decimal) --> #(diez işareti),  Boolean --> T|F , 
           # .. Coğrafik veri(country,region,state vs) --> (Dünya haritası simgesi), Cluster group--> Ataş işareti
           # Data source da verinizi canvas a atınca altta sütunların yanındaki bu simgelere tıklayarak veri tiplerini değiştirebiliriz
           # Verinizi canvas a atınca bu veri tiplerini kontrol etmekte fayda var
       # Dimensions: names, dates, titles, geographical data vs (DIKKAT: örneğin Id de burada yani dimensionda yer alacak çünkü
       # .. aggregate işlem yapmayacağız. Örneğin Id leri toplamamız bize herhangi faydalı bir bilgi vermez. O yüzden bu dimension
       # Measures : Profit, Sales, Salary vs
       
############################
# row-level record nedir?
    # Satır düzeyinde kayıt(row-level record) Tableau'da çok önemli bir kavramdır. Çünkü bir veri satırının hangi bilgileri 
    # .. içerdiğini anlamak çok önemlidir. Bu şekilde, verilerinize karmaşık sorular sormak için daha fazla güce sahip olacaksınız.
    # .. Satır düzeyindeki verileri anlamanın neden önemli olduğunu görmek için aşağıdaki "commuter" veri kümesini analiz edelim.
    # Note: "commuter", her gün evden işe gidip gelen bir kişidir.
"""
        Name	 Mode_of_Trasportation	Days_Per_Week
        Brandon	        Bus             	2
        Brandon	        Bicycle	            3
        Arthur	        Car	                2
        Arthur	        Bicycle	            1
        Arthur	        Walk	            2
        Isaac	        Car	                3
        Isaac	        Bicycle	            2
        """
    # Her satır, bir "commuter" ın işe gitmek veya eve dönmek için belirli bir ulaşım aracını kullandığı haftada kaç gün olduğunu 
    # .. gösteriyor. Ancak gezilerle ilgili bazı önemli ayrıntılara yer verilmemiş.
    # .. Örneğin, Brandon haftada iki gün otobüs kullanıyor ve işe gitmek için mi yoksa eve gitmek için mi kullandığına dair bir 
    # .. bilgi yok. Ayrıca, Brandon işe gitmek veya eve gitmek için tek bir yolculukta birden fazla araç kullanabilir. 
    # .. İşe gitmek için Otobüsü kullanabilir ve eve gitmek için yürüyerek gidebilir. 
    # Böylece, bir satırın ne tür bilgiler içerdiğini bilirsek, veri setimizi daha iyi analiz edebilir ve daha fazla veri toplama 
    # .. gereksinimlerini tespit edebiliri documentation avaiz. Örneğin, şunları bilmek istersek:
        # 1.Bir günde kaç kişi birden fazla ulaşım modunu kullanıyor?
        # 2.Otobüsle işe gitmenin ortalama uzunluğu ne kadardır?
    # Yukarıdaki bu soruları cevaplayabilmek için veri setimizi aşağıdaki gibi değiştirmemiz gerekiyor
"""
    Name	     Trip	 Start_Time	 End_Time	   Date	    Mode	Est. Distance
    Brandon	   To work	  07:30 am	 07:45 am	2020-05-13	Bus	      5 km.
    Brandon	  From work	  05:10 pm   05:45 pm	2020-05-13	Bicycle	  6 km.
    """

############################    
# Level of Detail    
    # İkinci veri seti birincisinden daha detaylıdır. İşte Tableau'da sıkça karşılaşacağınız bir diğer önemli kavram: Granularity. 
    # Tableau'nun terimi ile Granularity, ikinci veri seti, birinci veri setinden daha "granular"dır(Tanelidir/Ayrıntılıdır/Detaylıdır)  
    # Granülarity, nerede olursanız olun, bir veri parçasının ayrıntı düzeyini ifade eder. Veriler daha az ayrıntılı hale geldikçe,
    # ..  onu bir "aggregation" veya "aggregated data" olarak tanımlayabiliriz. "aggregation", Tableau'da da çok önemli bir kavramdır. 
    # .. "aggregation" terimini SQL derslerimizden hatırlayabiliriz. "aggregation", verilerin nasıl birleştirildiğini ifade eder. 
    # "aggregation" ve "granularity"(ayrıntı düzeyi), ters yöndedir.Yani;Daha fazla aggregation, daha az "granularity"(ayrıntı düzeyi),
    # .. daha az "granularity"(ayrıntı düzeyi), daha fazla aggregation anlamına gelir.
    # Önemli:  granularity veya aggregation düzeyi, verilere sorabileceğimiz soruyu ve verilerden elde edilen keşifleri etkiler.

############################
# CONNECT TO TABLEAU
# Connect --> Analyze --> Share

# Tableau ya girince; Start Page
# Connect kısmında 
    # "To a File" ya da "To a Server" kısmından verilerinize bağlanabilirsiniz
    # "More..." kısmından bulut sistemleri vs ye şirketiniz nasıl talep ediyorsa ona göre bağlantı yapabilirsiniz
    # .. bunlar için izinleriniz olması gerekiyor vs.
    # Burada "Open" kısmında ortada çalışmalarınız görünüyor(dashbordlar vs) eğer çalışmalarınız karmaşıklaştıysa, 
    # ..sizin için önemli çalışmanın üzerine gelerek "pin" leyebilirsiniz.
    # Saved Data sources ve Sample workbooks: Örnek data setler, workbooklar var. Bunlarla çalışılabilir
    # Sağ tarafta; Tableau nun eğitimleri, kaynakları, reklamları var
    # Sol üst "File" altındaki simgeye tıklayarak, "Data Source" page ve "Start page" arasında geçiş yapabiliriz

# Data Source Page
    # 3 e ayrılıyor
    # 1.Left pane : Sol taraftaki dikey kısma verilen isim. Bağlanılan veri kaynağını ve detayları(sheet names, table names) gösterir
    # 2.Canvas    : Sağ üstteki yatay kısma verilen isim. 2 tabakalıdır. 1.Logical layer 2. Physical layer. 
        # Logical layer  : Canvas logical layer ile açılır. Logical tables arasında ilişkiler kurabiliriz
        # Physical layer : Logical layerdaki bir tabloya çift tıklayarak physical layer a gireriz. Daha sonra physical layerdaki
            # .. tablolar arasına joinler ve union lar ekleyebiliriz
    # 3.Data Grid : Sağ alttaki yatay kısma verilen isim. Verimizin ilk 100 satırındaki detayları gösterir(sütunlar, değerler vs)

# Veri setine bağlanalım
    # Connect --> Excel --> Veri setini seçelim
    # Canvas üzerinde "Sample - Superstore" yazan yere tıklayarak verinin ismini değiştirebiliriz
    # Left Pane da - 
        # Connections kısmında; add den başka connection lar ekleyebiliyoruz.
        # .. Kaldırmak için "Connections" kısmında veriye--> sağ tık --> remove
    # Sheets kısmında; Üstte yazan orders-people-return bu excel içindeki sheetlerim
        # .. Üzerine gelerek yanındaki simgeye tıklayarak sheet leri inceleyebiliyoruz
        # .. Altta yazan Orders-People-Return kısmı "named range" fonksiyonlar varsa tableau bunları ayırrabiliyor
        # .. Ancak bu veri setimde böyle bir alan olmadığı için alttaki orders-People-Return kısmı üstekilerle aynı.

# Şimdi orders sheet i ortaya(canvasa) sürekleyelim
    # Tabloları combine ederken bazen join , bazen relationship vs kullanacağız. Bunun için canvas ı kullanacağız
    # Canvasda yazan orders ın üzerine geldiğimde bunu "logical table" olarak gösteriyor. "Physical table" a geçmek istersek 
    # .. Canvas da çıkan "Orders" a çift tıklamamız gerekiyor.
    # Çift tıkladığımızda yeni bir pencere açıldı bu kısımda physical table ve layer ı görüyoruz. Daha sonra detaylı bakacağız
    # .. Burada başka bir tablo atıp mesela "people" ı atıp "join" işlemi yapabilirim. 
    # People a sağ tıklayıp remove diyebilirim ya da bunu sürükleyip left pane e bırakabilirim
    # Çarpıya tıklayıp logical layer a dönelim
    # .. People ı atalım canvas a. Burada da bir relationship oluşturuyoruz
    # 2 si arasındaki fark: Joinlerde tabloyu fiziksel olarak birleştirip tek bir tablo haline getiriyor
    # Relation da ise 2 tablo arasında ortak field ları kullanarak bir ilişki belirliyor
    # People ı yine atabiliriz kenara. Ancak "orders" tablosunu atmış olsaydım, bu root table olduğu için canvas ı komple boşaltacak
    # Altta relationship in özelliklerini görebiliriz
    # People ı atalım şimdi kenara
    # Sağ üstte "live" ve "extract" diye 2 seçeneğimiz var.
        # "Live"    : Sürekli kullandığımız verisetinden beslenen bir model oluşuyor.
            # Veri setinde bir değişiklik yaptığımız zaman bu güncelleniyor.
        # "Extract" : Bağlantı kurduğumuz veri setini bir zipleme metodu ile "extract" ediyor
            # Extract a tıkladıktan sonra sol altta sheet e ve dashboard umuza tıklayınca kaydetme yeri açılıyor
            # .. Bizim tableau daki dosyalarımızı tableau kendi belirlediği bir uzantı(.hyper) ile zipliyor
            # Extract ı kullanacağınız zaman biriyle paylaşacaksanız "hyper" uzantılı dosyayıda da veri seti ile paylaşmanız gerekir
            # Extract a tıklayınca "edit" ve "refresh" diye bir bölüm daha açıldı
            # Edit    : Üzerinde çalışmak istediğim veri setini add diyerek -- > "order date" e göre filtreleyebilirim
            # Refresh : Bir sorun olduğunda bu butona basabiliriz
                # NOT: Şu anda localdeki bir dosyadan çalıştığımız için "live" ve "extract" arasında çok büyük bir fark olmayacak
                # Internetten çekeceğimiz bir veri seti üzerinde çalışsaydık veri çok büyük olabilirdi
                # .. Bu noktada extract alıp dosyaları zipleyerek kullanmak daha mantıklı
    # Yine altta veri setinin sağ üstünde rows 1000 yazarak 1000 satır görebiliriz
    # .. Veri setinin solunda details kısmından veri setinin ismini vs değiştirebiliriz
    
# Sheet kısmını geçelim sol attan
    # Solda left pane de measures ve dimesions lar haricinde tableau nun oluşturduğu default fieldlar var
    # .. "measure names", "Orders(Count)", "Measure Values", "Latitude(generated)", "Longtitude(generated)" gibi..
    # .. "Latitude(generated)", "Longtitude(generated)" , state , region gibi field larınız varsa belirir, her zaman belirmez
    # Üstteki işaretler Sıraylar
        # Geri, ileri, kayıt, yeni data source ekleme, Auto update-->auto çıktı vermeye yarıyo(basarsak eğer her bir view 
        # .. oluşturmaya çalıştığımızda sağındaki butona basmak zorunda kalırız), new-worksheet, duplicate(çalışmayı yeni sheet e 
        # .. kopyalama), clear sheet, swap-rows-columns, sıralama1, sıralama2, highlight(seçili olanı(bar ı mesela) highlight eder),
        # .. , T:labelları gösterir, fix axis(mesela columns a category nin yanına yeni bir sütun(subcategory) atınca axisi sabit 
        # .. tutuyor), Standart(fit widht, fit height, entire view, Normalde viewde grafiğin kenarından sağa- sola- yukarı- aşağı 
        # .. kaydırabiliriz istediğimiz gibi), show/hide cards(Ekranda kaybolan şeyleri geri getirmek için kullanabiliriz),
        # .. , presentation(genel bir bakış olarak kullanacağız sadece), paylaş(bunu kullanmayacağız bu tableau online ve tableau 
        # .. server da paylaşmak için kullanılır. Biz , bunun yerine server--tableau public-- save to tableau public as...  yapacağız)
    
########################################################################################################
#%% TABLEAU - 2
######################
# GIRIŞ - NOTLAR
# Tableau açıp bağlantı kuralım ve sheet1 e geçelim
# Tableau da "tables" kısmında dimensions lar mavi , measureslar yeşil görünüyor. ANCAK;
    # Measures   : Nümerik veriler. Üzerinde matematiksel işlemler yapabileceğimiz(OrderId kategorikti mesela)
    # Dimensions :  Kategorik veriler. Bunlar üzerinde de bazen aggregate function kullanabileceğiz. Birazdan göreceğiz

# NOT: dimensions lar discrete ve continuous olabilir
# NOT: measures lar discrete ve continuous olabilir
# NOT: Data dtype ı string ve Boolean olanları continuous yapamıyoruz Tableauda da normalde de

#######################
# VIEWS
# 1.View içerisinde oluşturduğumuz grafiklere de "view" diyoruz 2.Arka plana da(Figure-Subplot mantığı) view diyoruz

# Bir görselleştirme oluşturma şeklimiz, "fieldları" aşağıdaki resimde gösterilen alanlara yerleştirmektir
# .. Görselleştirme oluşturabileceğimiz alanlar şunlardır:
"""
Columns shelf
Row shelf
Pages shelf
Filters shelf
Marks Card
View
"""
# Not: Grafikler oluşturmak için "Show Me" özelliği de vardır. Bunu daha sonra göreceğiz.  
 
#######################
# VIEW(GRAFIK) OLUŞTURMA
# NOT: View oluşturmanın bir kaç yöntemi vardır
# Alttan new-sheet açalım

#########
# Way to Build a Viz(Nasıl viewler oluşturabiliriz)
# 1.Columns ve rows a sürükleyip
# 2.Drop alanlarına sürükleyip
# 3.Tables daki lere çift tıklayarak 
# 4.Using Show Me
# 5.Using Marks Card

#########
# View oluşturma - 1
# Sol tarafta "Tables" kısmındaki "Region" ı üstteki "columns" a sürükleyelim
# Sol tarafta "Tables" kısmındaki "Sales" i üstteki "rows" a sürükleyelim

#########
# View oluşturma - 2   
# Sol tarafta "Tables" kısmındaki "Region" ı ortadaki "drop field here" kısmında sütunların olduğu yere sürükleyelim
# Sol tarafta "Tables" kısmındaki "Sales" i ortadaki "drop field here" kısmında oluşan sütunun yanındaki satırlara
# .. sürükleyelim yani; "Central" ın altındaki "Abc" yazısının biraz soluna

#########
# View oluşturma - 3
# NOT: The order you double-click on Dimension or Measure matters in Tableau.
# Önce Sales'a çift tıklarsak, ardından Region'a çift tıklarsak, yukarda yaptıklarımızın aynısı gelir(bar chart)
# Önce Region'a çift tıklarsak, ardından Sales alanına çift tıklarsak, bir "text table" gelir.

#########
# View oluşturma - Diğer bir yol --> SHOW ME
# "Category" ye tıklıyoruz
# "Ctrl" ye basılı tutup "Sales" e tıklıyoruz
# Sağ üstte "Show me" kısmını tıklıyoruz.
# Bize önerilen grafik "kırmızı" çerçeve içinde ama bu değişkenler görmek istediğimiz başka türlerde seçebiliyoruz

#######################
# MARKS   
# Görselleştirme oluşturmanın başka bir yolu da Marks kartını kullanmaktır. 
# Alanları kartlara yerleştirerek işaretleri renk, boyut, şekil, metin ve ayrıntıyla kodlayarak görselleştirmeye
# bağlam ekleriz. Burada "marks" terimini kullandık. Bu çok önemli bir terim ve bunu sık sık duyacaksınız.
# Marks kartına geçmeden önce "mark" terimini açıklayacağız. 
# "Marks" ı veri noktaları olarak da düşünebiliriz. Tableau, veri kaynağımızdaki her işaretin bir satıra 
# .. (veya bir grup satıra) karşılık geldiği işaretleri kullanarak verileri görüntüler. 
# Örneğin; Category ve Sales alanlarını kullanarak bir çubuk grafik oluşturduğunuzda, üç kategoriyi temsil eden 
# üç çubuk alırsınız (aşağıdaki resme bakın). Her çubuk bir mark tır (veya veri noktasıdır). 
# Bu, görünümde üç mark(işaret) olduğu anlamına gelir. Tableau'da bir işarete atıfta bulunduğumuzda, 
# .. görselleştirmede verileri temsil etmek için kullanılan şekli kastediyoruz.

# NOT: Category ve Sales bar chart ı için tableau da en sol altta ne kadar "mark" var görebiliriz(3 marks).
# .. Sütun ve satır bilgisi vs de gösterdi
# NOT: Tableau, veri kaynağımızdaki her bir mark ın karşılık geldiği bir satıra (veya bir grup satıra) göre 
# .. verileri görüntüler.
    
#######################
# MARKS CARD
# "View" deki "mark" lara bağlam ve ayrıntı ekler.
# Category ve Sales bar chart ı için solda "profit" i "Marks" kısmının içindeki alanlara("Color", "Size" vs) 
# .. sürüklersek grafiğimize başka bir boyut eklemiş oluruz.(Hangi kategorimiz daha çok kar getiriyor(profitable) gibi)..
# Bunu yaptığımızda sağ üstte bize (sürüklediğimiz yere bağlı olarak) bir "legend"(Veri görselleştirmeden hatırlayacağız) gösterir
# "legend" ı sürükleyip solda "marks" ın altına , grafiğin soluna vs taşıyabiliriz
# Ayrıca "profit" i taşıyınca "Marks" ın altında "SUM(Profit)" yazısı oluştu. Yazının solundaki simgeye tıklayıp
# .. hangi mark türünü(label,size,detail,tooltip) görmek istiyorsak değiştirebiliriz
# Diğer bir konu tableau mark türünü otomatik olarak "bar" olarak belirlemiş. Ancak "Marks" altındaki "Automatic" kısmına
# .. tıklayarak bunu örneğin "Line" a çevirebiliriz. Üst tarafta araç çubuğundaki "T" simgesine tıklayarakda değerleri görebiliriz
# Profit i "color" a sürükledik diyelim. Rengi değiştirmek için -- > Color -- > Edit Color -- Palette(renk seçimi) -- > Apply
# Size: markların boyutlarını değiştirebiliriz
# Label: --> show mark labels
# Detail: 
# Tooltip: Burada yazan etiketler yerine başka bir şey yazıp sonra mouse ile barlar üzerine geldiğimizde o yazı görünür. Ayrıca
# .. bir alana tıklayalım orada sonra üstteki imleci sağa-sola çekerek yazının durması gerektiği ayarlayabiliriz
    
#######################   
# CHART TYPES
# Introduction to Charts
# Oluşturduğunuz görselleştirme (veya viz) şunlara bağlıdır:
    # Sormaya çalıştığınız sorular
    # Verilerinizin özellikleri
    # Içgörülerinizi başkalarına nasıl sunmak ve iletmek istiyorsunuz?
# Örneğin, her yıl satışlardaki büyümeyi göstermek, indirimli ürünler ile karlılık arasındaki bağlantıyı göstermekten 
# .. farklı bir görselleştirme gerektirir
# Tableau da neyi göstermeniz gerektiğini bilmek, onu nasıl göstermek istediğinizi belirlemenize yardımcı olacaktır
# Deneyimle, oluşturmak istediğiniz grafik türünü daha hızlı değerlendirebileceksiniz. Tableau esnek olduğundan, kalıpların 
# ..dışında düşünmenizi öneririz. Ancak, kutunun dışında düşünmeden önce, bazı yaygın grafik türleriyle başlamak faydalı olacaktır

#######################
# 1.Change Over Time
# Satış verileriniz var ve satışlarınızın zaman içindeki trendini görmek istiyorsunuz. 
# Bir "measure" ın için zaman içindeki değişimi göstermek, temel görselleştirme kategorilerinden biridir
# Zaman içindeki değişimi göstermek için, değişmesini beklediğiniz değeri ve Tableau'daki Date alanlarıyla nasıl 
# .. çalışacağınızı bilmeniz gerekir.

# Görselleştirmek için hangi grafik türlerini kullanırız?
    # line charts 
    # slope charts
    # highlight tables   
#  Change Over Time chart ne tür sorulara cevap verebilir?
    # Bu "measure" geçen yıl nasıl değişti?
    # Bu "measure" ne zaman değişti?
    # Bu "measure" ne kadar hızlı değişti?
 
#######################      
# 2.Correlation   
# Bazen iki değişkeniniz olur ve aralarındaki ilişkiyi ararsınız. Örneğin, sınıf büyüklüğü ile okul mezuniyet oranı arasındaki ilişkiyi
# ..  veya akciğer kapasitesinin dayanıklılıkla ne kadar ilişkili olduğunu arıyor olabilirsiniz. 
# NOT : Korelasyonun her zaman nedenselliğe eşit olmadığını unutmayın
# NOT : Korelasyonun gücünü göstermek için Tableau'nun "analytics objects" kullanabilirsiniz.     
# Mesela veriyi yükledik, sales ve category yi görselleştirdik(Bunları biliyoruz). Sol üstte "data" nın yanında "Analytics" var
# .. Ona tıklayıp ...

# Görselleştirmek için hangi grafik türlerini kullanırız?
    # scatter plots
    # highlight tables
# Bu çizelge ne tür sorulara cevap verebilir?
    # Bu iki "measure" birbiriyle ilişkili mi? Ne kadar güçlü?
    # Bazı "measures" diğerlerinden daha mı ilgili?
    # Bu "measures" ne kadar güçlü bir şekilde ilişkilidir?
      
#######################   
# 3.Magnitude  
# iki veya daha fazla ayrı öğenin göreli boyutunu veya değerini gösterir. Farklı bölgeler için satışları karşılaştırıyorsanız, 
# .. manitude(büyüklüğe) bakıyorsunuz.

# Görselleştirmek için hangi grafik türlerini kullanırız?
    # bar charts
    # packed bubble charts
    # line charts.   
# Bu çizelge ne tür sorulara cevap verebilir?
    # Bu boyut üyelerinden hangisi en yüksek ölçüme sahiptir?
    # Istisnai boyutlar var mı?
    # Bu boyutlar arasında en düşük ve en yüksek ölçü arasında ne kadar büyük bir boşluk var?   

#######################
# 4.Deviation
# Deviation(Sapma) çizelgeleri, bir değerin ortalama veya medyan gibi bazı taban çizgisinden ne kadar farklı olduğunu gösterir. 
# Hangi öğelerin alışılmadık derecede yüksek veya düşük kâr marjına sahip olduğunu bilmek istiyorsanız, bir sapma tablosu kullanırsınız.
# Sabit bir referans noktasından varyasyonları (+/-) vurgularlar. Tipik olarak referans noktası sıfırdır, ancak aynı zamanda bir hedef 
# ..veya uzun vadeli bir ortalama da olabilir. Duyguyu göstermek için de kullanılabilir (olumlu/nötr/olumsuz) 
# Örnek : Bir iklim değişikliği projesi üzerinde çalışıyorsunuz ve ortalama sıcaklıktan sıcaklık değişimlerini göstermek için..    

# Görselleştirmek için hangi grafik türlerini kullanırız?    
    # bullet charts 
    # bar charts
    # combination charts
# NOT: Ayrıca bir Z-skoru kullanarak sapmanın istatistiksel önemini de bulabilirsiniz.
# Bu çizelge ne tür sorulara cevap verebilir?
    # Bu "measure" normdan ne kadar uzaklaşıyor?
    # Bu "measure" daki sapmalar ne kadar önemlidir?
    # Sapmalar için bir desen("pattern") var mı?    

#######################    
# 5.Distribution
# Bir popülasyondaki olayların sıklığını bulmaya çalışırken dağılıma bakıyorsunuz.
# Örneğin Yaşa göre bir ankete katılanların sayısını veya günlere göre gelen aramaların sıklığını gösteriyorsanız, 
# .. bir dağılım grafiği en iyi seçim olabilir.

# Görselleştirmek için hangi grafik türlerini kullanırız? 
    # Histograms
    # Population pyramids
    # Pareto charts
    # Box plots.
    
# Bu çizelge ne tür sorulara cevap verebilir?
    # Olaylar belirli bir olasılık etrafında kümeleniyor mu?
    # En çok hangi nüfus grubu satın alıyor?
    # İş günümüzün en yoğun saatleri ne zaman?
    
#######################
# 6.Ranking  
# Bazen sadece bir değerin büyüklüğünü değil, aynı zamanda boyutunuzun tüm üyelerinin göreceli sıralamasını da tasvir etmek isteriz
# llk 10 satış görevlisini veya düşük performans gösteren durumları göstermek için bir sıralama tablosu kullanılır

# Görselleştirmek için hangi grafik türlerini kullanırız? 
    # bar charts(top n tanesini seçip sıralama ile)
    
# Bu çizelge ne tür sorulara cevap verebilir?
    # Şirkette düşük performans gösteren kaç kişi var?
    # İlk on müşterimiz tarafından ne kadar gelir elde ediliyor?
    # En düşük gelirli on mülkümüzün değeri nedir?  

#######################    
# 7.Part-to-Whole   
# Part-to-Whole(Parçadan-Bütüne) çizelgeleri, tek bir parçanın bir bütünün ne kadarını kapladığını gösterir. 
# Örneğin, her bölgenin toplam satışlara ne kadar katkıda bulunduğunu veya her bir farklı nakliye modunun tek bir ürün için ne 
# .. kadar pahalı olduğunu gösteriyorsanız, bir parçadan bütüne bir tablo kullanırsınız.    

# Görselleştirmek için hangi grafik türlerini kullanırız? 
    # pie charts 
    # area charts
    # stacked bar charts
    # treemaps

# Bu çizelge ne tür sorulara cevap verebilir?
    # Bu değer toplama ne kadar katkıda bulunuyor?
    # Maliyetlerin dağılımı her yıl nasıl değişiyor?
    # Farklı kalemler bölgelere göre satışlara farklı miktarlarda katkıda bulunuyor mu?

#######################
# 8.Spatial
# Spatial(Uzaysal/Mekansal) grafikler, verilerinizdeki konumları ve coğrafi modelleri kesinleştirebilir.
#  En çok yaya trafiğine sahip havalimanı terminallerini veya ülke genelindeki tüm satışların bir haritasını göstermek, 
# .. Spatial haritalara örnektir.

# Görselleştirmek için hangi grafik türlerini kullanırız? 
    # filled maps
    # point distribution maps
    # symbol maps
    # density maps
    
# Bu çizelge ne tür sorulara cevap verebilir?
    # En çok satış hangi ilde?
    # Müşterilerimiz dağıtım merkezlerinden ne kadar uzakta?
    # Hangi kapıya kaç kişi geliyor?

#######################    
# 9.Flow
# Flow(Akış) çizelgeleri, Sankey diyagramları gibi zaman içinde hareketi ileten haritalar olabilir. Flow haritaları,
# ..  zaman içindeki yolu(path) ya da  başlangıç ​​ve hedef çizelgeleri arasındaki yolu(path) içerir.   

# Görselleştirmek için hangi grafik türlerini kullanırız? 
    # ... (Pre-class da belirtilmemiş)(Flow maps)    

# What types of question can this chart answer?
    # What is the longest shipping route?
    # How long are people lingering around gates?
    # What are the bottlenecks to traffic in the city?

#######################
# DATES
# Tarihler "dimensions" dır. ve her zaman  veri bölmenizin "dimensions" bölümünde görünürler. Unutmayın, bir "dimensions" olmak 
# .. her zaman kesikli/ayrık(discrete) oldukları anlamına gelmez. Aslında, ikisi de(kesikli veya sürekli) olabilir.

# Dates, Tableau içinde iki farklı veri tipinde gelebilir. Tablo tarihi simgesi "date" ve Tablo tarih ve saat simgesi "date" ve "time".
# Diğer veri türlerinin çoğundan farklı olarak, bu iki farklı tarih türü birbirinin yerine kullanılabilir. 
# Bir "date" veri türünü ve "date" ve "time" veri türünü karıştırırsanız, Tableau, herhangi bir hesaplama amacıyla date alanının 
# .. time öğesini 12:00:00 AM olarak varsayacaktır.

# Bazı grafik türleri("line chart" veya "area graph" gibi) bir tarih alanı kullanıldığında en iyi performansı gösterir.
# .. Ayrıca, bazı tablo hesaplamaları  "YTD(Year to Date) deki büyüme" veya "YTD Toplamı" gibi bir tarih alanı gerektirir.

# Tarih alanları yukarıda bahsedildiği gibi kesikli veya sürekli olabilir. Farkı anlamak için önce tarih bölümlerinden 
# .. ve tarih değerlerinden bahsedelim. Kesikli tarihler, tarih bölümlerini kullanır. 
# Tarih bölümleri, kelimenin tam anlamıyla bir tarihi oluşturan parçalardır. 6 Mart 2016 tarihini alalım.
# ..  “Ay” tarih kısmı Mart (veya 03). "Gün" tarih kısmı 6 ve "yıl" tarih kısmı 2016'dır. 
# Örneğin: The "month" date part of 14-01-2020 is January (or 01)
# .. Bunlardan herhangi birini kendi başıma kullansaydım, mesela bir ay, o zaman mesela Mart aylarına(Tüm yıllardaki) topluca bakmış olurdum

#######################
# Discrete vs. Continous
# Dimensions ve Measures diye fieldları 2 ye ayırmıştık

# Discrete   : Kesikli veri. Field a atınca her bir unique değerini axis de görüyoruz
    # Product Category, Segment, Country, Age vs
# Continous  : Sürekli veri. Fielda atınca bize aralıklı bir axis çıkartıyor
    # Revenue, Population, Profit vs

# Discrete: Üstteki cümlenin aynısı discrete için kullandık;
# Bunlardan herhangi birini kendi başıma kullansaydım, mesela bir ay, o zaman mesela Mart aylarına(Tüm yıllardaki) topluca bakmış olurdum

# Continous :  Veri kümem 2012'den 2017'ye kadar olan verileri içeriyorsa, bu Ocakların tümü Ocak ayı için bu ayrı sütunda toplanır.
# Sürekli bir tarih olması durumunda, bir zaman çizelgesi oluşturur. Tarih değerleri, zaman çizelgemizin nasıl düzenlendiğini belirler
# Bir araya getirilen tüm Ocaklara bakmak yerine, Ocak 2017 veya Ocak 2018 gibi belirli bir Ocak ayına bakıyoruz.

# Sonuç : Discrete i bir bar chart ta düşünebiliriz, x ekseni Month(tüm yıllar), y ekseni "sales"
#         Continous da bir line chart düşünebiliriz, x ekseni ay ve yıllara göre belli aralıklarla 
# .. olan değerler(2012 Eylül, 2012 Aralık, 2013 Ocak, ... 2017 eylül gibi) , y ekseni "sales"

#######################
# ÖRNEKLER

####### Örnek1 : Sub category bazında satış ve profitler
# Columns : Sub-Category
# Rows    : Sum(Sales), Sum(Profit)
# Sıraladık. Default olarak bar charttayız
# Not: 2 grafiktede değişiklik istiyorsam -- > marks --> all --> ...
# Rowsda profit --> Sağ tık --> Dual axis(Tek eksene/grafiğe düştü).. Sol da "sales" sağ da "profit" ölçeği
# Marks kısmından 2 sinide bar chart yapalım
# Sağda kalan axis e(profit in axisine) -- > sağ tık --> synchronize axis .. Önceden profit değerleri sağdaki axisi baz
# .. alıyordu yani kendi axisini, synchronize yapınca sales in axisine göre şekillendi profit bar ı
# Sağ taraftaki axis --> sağ tık --> show header ı kaldıralım .. Tek axis imiz var artık
# Bunu geri getirmek istersem rows da profit  --> sağ tık --> show header
# Profit değerlerini line chart yaptık
# entire view
# legend ı sola alalım. Edit color -- > sales --> mavi , profit --> kırmızı yapalım 
# Soldaki axis e -- sağ tık --> edit axis(ya da direk çift tık) -- > Title --> (axis ismini değiştirelim) --> Sum & Profit
# Sadece sales a label koyalım. Sales field ını mark kartındaki label a sürükledik
# Labelları formatlayalım -- > herhangi bir bara sağ tıklayalım --> Format -->( Solda gelen ekranda hemen değişiklik yapmayalım.
    # .. Bu bir hatadır. Önce ilgili olan field ı seçmemiz gerek) --> Fields --> Sum(sales) --> (Solda axis ve pane seçenekleri geldi)
    # .. 2.Yol(Kolay) : Rows da sales --> sağ tık --> format
    # .. Axis: Buradaki şeyleri değiştirirsek axisteki değerleri etkiler
    # .. Pane: Buradaki şeyleri değiştirirsek grafikteki değerleri etkiler. Bizim amacımız da burası
    # .. Pane --> default kısmındaki --> numbers --> Currency(custom) -- > decimal ı 0 yapalım -- > (negative fields negative değerleri gösterme formatı)
    # .. --> Display units --> thousands diyelim görmek için() -- > prefix  -->  "$" yazalım(sola) --> 
    # .. include thousands seperatory--> noktayı vs kaldırmaya yarar
    # NOT: File - workbook locale -- > More --> United States --> Böyle yaparsak tl yerine dolar işareti otomatik gelir.
    # .. Tarih formatları, ya da paraların nokta ile mi yazımını vs değiştirir
    # .. font --> 12 yapalım, Bolt yapalım -- > Alignment --> Labelların konumu(sağa yasla , sola yasla vs , yazım şekli yatay-dikey,
    # .. label ın belirdiği yer(bar ın üstünde mi içinde mi vs))
# Alttaki axis yazıları için --> sub category -- sağ tık --> format -- > header--> font --> 12, bolt vs vs
# Grafiğin üstünde yazan "sub category" --> sağ tık -- > hide field labels for columns
# Sheet -1 ismi değiştirelim sol alttan -- "Dual axis" diyelim
# Sonra grafiğin üstünde "dual axis" yazısı geldi(title ım) --> çift tık(ya da sağ tık - edit title) --> yazanı silip kendimiz isim verelim
# .. -> sales and Profit by Sub-Categories --> Mouse ile bu yazıyı seçip -- > 12, Bolt, Renk, konumunu değiştirelim
# Şimdi grafik tamam ancak bir insight çıkartmamız gerekiyor
    # view da(canvas da boş yerde) --> sağ tık --> area --> Tables are non-profitable although they are high in sales --> OK
    # .. Ekranda yazı geldi. Bunu sağından solundan çekip  büyütüp küçültebilirim. Tutup istediğim yere sürükleyebilirim
    # .. Buna tıklayıp --> sağ tık --> format -- > box--> border -- > düz çizgi --> Renk seçelim -- > corners-- more rounded
    # .. burada "line" kısmında da işlemler yapabiliriz ama burada bir "line" durumu yok
    # Profit line ında table ın olduğu noktaya --> sağ tık --> annotate --> mark --> (gelen otomatik ifadeye) OK diyelim
    # .. Tekrar çift tıklayarak değiştirelim --> sadece profit yazan kısmı alalım -- ortalayalım --> OK
    # .. Buna da sağ tıklayıp --> formatlayalım -- > (burada line kısmını formatlayabiliriz)
    # .. buna yine tıklayıp buradaki line ı oynatamıyoruz(DIKKAT. Aşağıda "point" de bunu oynatabileceğiz)
    # Barlardan birine -- > sağ tık -- > annotate --> point -- >OK --> çizginin başladığı yer y ekseninde olduğu yeri gösteriyor tam 
    # .. sağ tık --> format --> vs vs..
    # .. Bunun üzerine tıklayıp line ı istediğim yere çekebilirim burada
    
####### Örnek2 : Lolipop grafiği
# Columns : Sub-Category
# Rows    : Sum(Sales), Sum(Sales)
# sıralayalım(default bar. Barları sıralayacağız)
# sağ taraftaki eksen --> sağ tık --> dual axis
# 1. sales --> bar
# 2. sales --> circle
# synchronize axis yapalım ve show header kapatalım(sağdaki)
# solda measures dan profit --> circle olan sales --> label a -- format ile yuvarlağın içine gelsin
# solda measures dan profit --> circle olan sales --> color --> legend geldi --> çift tık --> profit positif değerler yeşil, 
# .. negatif değerler kırmızı olacak şekilde 2 renk
    # NOT: bu legend da renk değiştirirken advanced diyerek. Rengin ayrılacağı değer noktasını belirleyebilirim(başlangıç-bitiş) , ya da 
    # .. direk alttaki "center" kısmından
# Bar ın rengini ayarlayalım
# size ları düzenleyelim - barlar küçük -- toplar büyük olsun
# NOT: Burada circle olan sales de marks a gelip --> shape i seçince tooltip in yanında "shape" card ı oluşacak --> (Buna tıklayıp
# .. cirlce yerine farklı shape ler koyabiliriz grafiklere--> (Ayrıca istediğimiz bir resmi koyabiliriz) 
# .. Bunun için ; --> file --> repository location --> My tableau repository --> shapes --> (Burada yeni klasör oluşturup kendi görsellerinizi
# .. atabilirsiniz) --> (Daha sonra tableau ya dönüp) --> marks da circle olan sales de --> shapes --> more shapes --> reload shapes -->
# .. --> (Artık attığımız şey klasörde görünecek) --> sonra bunu "select shape palette" kısmından seçiyoruz
# .. Daha sonra eğer soldan "sub category" yi ben marksda circle ı değiştirdiğim sales in shape ine sürüklersem her bir category 
# .. için farklı bir shape çıkacak --> shape e tekrar tıklayarak sub-categorynin shape ini ayarlayabilirim

####### Örnek3 : scatter plot örneği(Sales-profit)
# Columns : Sun(Sales)
# Rows    : Sum(profit)
# Tableau otomatik aggregation yaptı. Sales ların toplamı ve profit toplamını aldı tek değer getirdi
# Her bir satır için tek nokta görelim -- > üst menü --> analysis --> Aggregate mesaures(tik kaldıralım)
    # Sol attan kontrol 9994 marks
# columns ve rows daki sum(Sales) ve Sum(profit) --> sales ve profit e döndü
# aggregate measures tikini kaldırmadan eğer category yi --> marks da detail cards ına sürüklersem
# .. her bir kategory için sum ve profit toplamlarını getirecek 3 nokta oluşacak
# .. level of detail i arttırmış oldu
# Şimdi "sub category" yi tutup marks da duran "category" nin üzerine getirirsek onu çıkaraıp yerine sub-category yi koyacak
# Peki her bir satırı ifade eden sütunumuz hangisi? Onu detail kısmına atalım ve 9994 marks görelim --> RowID
# profite göre renklendirelim -- > profit i color card ına

####### Örnek4-1 : Date
####
# Rows : Order Date
# Default bir DATEPART seçti (Year)
# Diğer fieldlardan farklı olarak buradaki "YEAR(Order Date)" in başında bir "+" işareti var
    # .. buna tıklayınca bir alt DATEPART ı getirecek(quarter) --> QUARTER(Order Date) de "+" ya tıklayalım
    # .. MONTH(Order Date) geldi.. Tekrar tık --> DAY(Order Date) .. Elimizde saatte olsaydı daha da inebilirdik
    # Burada sadece DAY(Order Date) i bırakalım diğerlerini attık 
# Sales --> "Abc" yazan yere atalım. Satış toplamlarını attık
    # Veri setindeki her bir ayın 1 günü ,2 günü ,... ,30 günü için satış toplamlarını getirdi
    # Sonuç olarak biz bunu burada "DISCRETE" olarak kullanmış olduk

#### Örnek 4-2 
# Veri setimin ilk gününden son gününe kadar olan kısmı görmek istiyorum ben diyelim. Sayfayı temizleyelim 
# Rows: Order Date --> YEAR(Order Date) --> sağ tık --> 
    # .. Şimdi ortadan 2 çizgi ile ayrılmış şekilde "year, quarter .. vs" var üstte altta da "year, quarter vs" var
    # .. Üsttekiler --> DISCRETE , Alttakiler --> CONTINUOUS
    # Alttakilerden "Day" e tıklayalım .. Üstte rows kısmında rengi değişti(yeşil oldu).Yani "CONTINUOUS" oldu ve
    # .. DAY(Order Date) oldu. Bu bar chart gibi görünüyor ama mouse ile üstüne gelirsem her bir datapoint için değerleri
    # .. görebiliyoruz. Sonra bunu şu an "DISCRETE" yapmak istiyorum.
    # .. rows da DAY(Order Date) --> sağ tık --> Discrete --> Sonra sales ı --> Abc kısmına bakabilirim

#### Örnek 4-3 
# Exact Date ile yapma. Sayfayı temizleyelim
# Rows: Order Date ANCAK BUNU SAĞ TIKA BASILI TUTARAK ALIYORUM
# Bir pencere açıldı. Üsttekiler yine discrete, alttakiler continuous. Yukarıdakinin aynısını yapabilirim
# Bu pencerede En üstte Order Date(Continuos) , Order Date(Discrete) var.
# Order Date(Discrete) dersek exact date leri discrete olarak getirecek
# Order Date(Continuos) dersek exact date leri continuous olarak getirecek

#### Örnek 4-4 
# Rows: sağ tık ile continuous DAY(order date) --> sağ tık --> Discrete
# Columns : sales
# Default line geldi sales in mark ı bar chart yaptık
# Sıraladık. En çok satış yapılan günleri görüyoruz

# Bunun 2. yolu
# Rows: sağ tık ile continuous MDY(Order Date)
# Columns : sales
# Default line geldi sales in mark ı bar chart yaptık
# Sıraladık. En çok satış yapılan günleri görüyoruz

#%% TABLEAU - 3
######################
# Table of Contents
    # What is Dashboard
    # Share Your Data
    # Filtering Your Data

############################################
# 1.What is Dashboard
# Genelde birden fazla sheet kullanılarak oluşturulan görselleri tek bir alanda gösteren görseller

############################################
# 2.Share Your Data
# TWB vs TWBX
    # Twb olarak kaydedersiniz çalışmanızı tekrar o çalışmayı açtığınız bilgisayarda sizin o datasetinizin de olması lazım
    # Örneğin; Siz birisiyle twb olarak paylaşsaydınız çalışmayı, excel dosyasını da paylaşmak zorunda kalırdınız
    # Twbx olarak kaydedersek çalışmayı, bunu gönderdiğim kişinin bilgisayarında tableau varsa bu dosyayı açıp sorunsuz çalışabilir
    # Twbx i dashboard olarak paylaşabilirsiniz veya tableau public üzerinden paylaşabilirsiniz

# Bir kaç sheet oluşturup daha sonra dashboard oluşturup bunu tableau public üzerinden paylaşacağız
#####################
#### Sheet - 1 
# Columns : Category, Sub-Category
# Rows    : Sum(Sales)
# Büyükten küçüğe sıralayalım
# Measures da profit --> color kartına bırakalım. 
# Measures da sales  --> label kartına bırakalım
# Sağ üstte --> legend --> stepped color --> 2 renk --> (pozitif ve negatif (profit)değerlere göre renklendirelim)
# sheet e isim verelim --> "Subcategory" diyelim
# Grafiğin üstünde de "Subcategory" yazdı. Bunu müşteri görecek. Buna --> çift tık --> "Sales and Profit by Subcategory" yazalım
# Grafiğin üstünde "Category/Subcategory" yazan yere --> Sağ tık --> Hide field labels for columns

#### Sheet - 2
# State --> Canvas ın ortasındaki "drop field here" a sürükleyelim. Harita geldi
# Country/Region ı aynı yere sürükleyelim. State lerin hangi ülkeye ait olduğunu biliyor artık tableau
    # 2. yol: Sadece State i canvas a attığımızda sağ altta "49 unknown" yazıyor --> Tıklayalım 
    # .. --> edit locations --> united states seçelim --> OK
# Üstte columns da oluşan "Longtitude(generated)" --> ctrl ye basılı tutup bunu sağa sürükleyip columns da bir tane daha 
# .. "Longtitude(generated)" oluşturduk
# Soldaki grafikte sales a göre renklendirme işlemi, sağdaki grafikte circle ları profitlere göre renklendirip tek 
# .. grafikte birleştireceğiz
# Mark kartında üsttekini(yani columns da duran soldakini aslında) seçip --> sales ı color kartına sürükleyelim
# Diğer mark kartında profit --> color kartına sürükleyelim --> "Automatic" kısmını "circle" yapalım
# columnsdaki Longtitude(generated) a --> sağ tık --> Dual axis
# Profiti attığımız mark kartında --> color --> border -- > siyah rengi seçelim --> (circle lar daha belirgin oldu)
# Profit arttıkça circle büyüsün .. Profit i  --> Profiti attığımız mark kartında --> size kartına sürükleyelim (Sağda legend çıktı)
# .. Size a tıklarsak circle ların boyutunu ayarlayabiliriz
# Sales legend ında--> purple paletini seçtik
# Profit legend ında --> stepped color 2 --> (positive ve negatif değerlere göre 2 renk belirleyelim)
# sheet e isim verelim --> "Map" diyelim
# Grafiğin üstünde de "map" yazan yere --> çift tık--> "Sales and Profit by State"

#### Sheet - 3
# Rows    : State ..(Uyarı gelirse--> add all members)
# Columns : Sağ tık ile basılı tutarak customerID yi columns a --> CNT(Customer ID)
    # 2. yol CustomerId yi columns sürükleyelim --> Sonra columnsdaki CustomerID ye --> sağ tık --> measure-->count
# Büyükten küçüğe sıralayalım 
# Labelları gösterelim
# Unique müşterileri görmek istiyoruz .. columns da CNT(CustomerID) --> sağ tık --> measure --> CNTD(CustomerID)
# Büyükten küçüğe sıralayalım  
# Profitleri de görmek istiyoruz .. Profit i color kartına sürükleyelim
# Legend dan yine 2 stepped color yapalım. Renkleri değiştirelim
# sheet e isim verelim --> "Customer"
# Grafiğin üstünde de "Customer" yazan yere --> çift tık--> "Number of Customers And Profit by States"

#### Sheet - 4
# Region a basıp --> Ctrl --> Profit ... Bu ikisini seçmiş olduk
# Show me kısmında -- Pie chart
# Boyutunu ayarlamak için pie chart ın kenarlarındaki görünmez yerlerden sağ sola, yukarı aşağı çekelim ya da
# .. üstte standart yazan yerden entire view vs diyebiliriz
    # 2. yol: Ctrl ye basılı tutarak -- sağ ve yukarı basarsak büyür, sol ve aşağı basarsak küçülür
# Region ı label a sürükleyelim
# profit i label a sürükleyelim
# Çıkan labellara(Yazılara) tıklayıp pie chart ın içine sürükleyelim
# Legend a geldik --> renk belirleyelim
# # sheet e isim verelim --> "Pie"
# Grafiğin üstünde de "Pie" yazan yere --> çift tık--> "Profits by Region"

#### Dasboard oluşturma
# Bu 4 sheet i kullanarak dasboard oluşturalım
# Alttan "new dashboard" simgesine tıklayalım
# Sol tarafta sheetlerimiz görünüyor
# Bu sheetleri sürükleyelim ortadaki canvas a 
# Bunları istediğimiz gibi konumlandıralım 4 sheet i tek bir view de
# Legendların bazılarını kaldırabiliriz istersek
# Pie chartta yazılar bozuksa "Pie" sheet ine dönüp düzenleyebiliriz
# Sol taraftan Size ı ayarlayabiliriz

#### Dashboard paylaşma
# Tableau Desktop professional da --> Üst menü de --> Server --> Tableu public --> Save to Tableau public as...
# .. --> (Sign in) --> HATA.(Verilerimiz extract etmeliyiz önce)
    # Tableau Public --> Üst menü de --> File --> Save to Tableau Public as... --> (Public de hata vermez)
# Data source a gelelim --> sağ üstte "extract" tıklayalım. Sonra sol attan dashboard umuza
# .. tıklayalım klasör penceresi açıldı --> Bu verisetini "hyper" uzantılı bir dosyada extract ediyor -->
# .. --> kaydet
# Şimdi tekrar Server --> Tableau public --> Save to Tableau public as... --> (sign in) --> 
# .. isim girelim "My First dashboard" -- > Save --> (browser da otomatik açılmalı). ya da hesabımıza girip görebiliriz

#### Browser da Tableau public kısmındayız
# Dashboard umuz görünüyor
# Altta details e tıkladığımızda Title ı vs değiştirebiliriz
# Sağ üstte resmin üzerine tıklayalım -- > my profile --> dashboard umu görüyorum
# .. Followingler favoriler , kaç kişi gördü vs var burada
# .. Sağ tarafta "create a viz" e tıklarsam browser da tableau penceresi açar
# Oluşturduğunuz dashboard un sağ altında "..." işareti var tıkladığımızda
# .. "show viz on profile" : Bu viz i profilimden gizleyebilirim istersem, 
# .. "viz on profile"      : Istediğim vizleri(Bu vizi) profilimde yukarda görünmesini sağlarım açarsam
# .. "delete" this viz"    : Bu biz i silebilirim 
# Sağ üstte -- > Discover --> Insanların yaptığı çalışmaları izleyebiliriz

############################################
# 3.Filtering Your Data
# Birden fazla filtre tipimiz var. Filtrelerin işlendiği sıraya göre bunları görelim.Yani filtrelerin uygulanma sırası
# Ayrıca bazı filtrelerin arasında ara katman gibi bir kısım var
# Hoca: Buna çok sık bakmak zorunda kalacaksınız. Burası önemli
    # 1.Extract Filters
    # 2.Data Source Filters
    # 3.Context Filters
        # Ara katman filtre --> Sets, Conditional filters, top N, Fixed LOD
    # 4.Filters on Dimensions
        # Ara katman filtre --> Include/Exclude LOD, data blending
    # 5.Filters on Measures
        # Ara katman filtre --> Forecasts, table calcs, clusters, totals
    # 6.Table Calc Filters
        # Ara katman filtre --> Trend lines, reference lines
    
# NOT: Extract ve Data source filters a bakmadan önce dimension filter ile alakalı bir şeye bakalım 
# Columns: Sum(Sales)
# Rows   : Sub-Category
# Büyükten küçüğe sıralayalım
# Mouse ile tek bar ı seçebilirim bar a tıklayarak ya da mouse a basılı tutup kaydırarak 3-4 tane barı da seçebiliriz
    # 2. yol: Tek bir bar a basıp daha sonra Ctrl ye basılı tutup başka barları da seçebilirim
# En üstteki 2 sini seçelim. Bir pencere açıldı
    # Keep Only : Sadece o 2 bar ı view de gösterir
    # Exclude   : Seçtiğimiz 2 bar hariç diğer barları view de gösterir
# Yani filtre ile uzun uzun uğraşmak yerine bazen böyle seçeneklerde var

######################
# 1.EXTRACT FILTERS
# Bunu data source page den yapıyoruz. Bunu mesela veriniz çok fazladır ve 20 yıllık veri içeriyordur. Siz sadece
# .. son 2 yıllık verilerle çalışmak istiyorsunuzdur o yüzden bunu kullanabilirsiniz. Daha az veriyle çalışacağımız için
# .. bilgisayarın hızı da artacaktır
    # Sağ üstte "extract" a tıklayalım --> edit --> "add" e tıklayarak yeni bir filtre ekleyebiliyoruz
    # .. --> Örneğin "order date" i seçelim" -- > OK --> Years --> Next -- 2020 ve 2021 i seçelim --> OK --> OK
    # Artık bu yılları filtrelemiş olduk.Sheet açıp Order date i columns a sürüklersek sadece bu 2 yılın kaldığını görebiliriz
    # Filtreyi kaldırmak için: data source --> edit(extract a tıklı olunca beliriyor) --> "Year of Date" yazan kısmı seçip --> Remove

######################
# 2.DATA SOURCE FILTERS
# Extracttan farkı, Extract daha önce işlem görüyor, diğer fark extract filters da sizin filtrelediğiniz verileri "extract" ediyor
# .. data source filter bu extract edilmiş filtreler üzerinden filtreleme işlemi yapıyor
# Bilgisayar performansını arttırmak için extract filters ve data source filters kullanılabilir
    # Data source --> Filters ın altında "Add" --> Açılan pencerede "Add" --> order date --> OK --> Years --> Next --> 2018 --> OK-->OK
    # Sheet e baktığımızda order date i columns a atarsak sadece 2018 in verileri olduğunu görüyoruz

######################
# 3.DIMENSION FILTERS
# Dimensionlar kullanılarak oluşturulan filtrelere denir
    # Sub-Category ye göre bir filtreleme işlemi yapalım
    # Columns : SUM(Sales)
    # Rows    : Sub-Category
    # Büyükten küçüğe sıralayalım
    # Sub-category yi filters kartına sürükleyelim. Bir pencere açıldı
        # General
            # Istediğimiz sub-category yi seçip filtreleyebiliriz
            # Summary kısmında --> Burada da dimension filtresi içinde filtreleme sıralamasını görüyoruz.
                # Selection(general) --> wildcard  --> Condition --> Limit(top)
            # Not: Filtrelemeden sonra filtersdaki Sub-category ye --> sağ tık --> show filters --> legend olarak sağda geliyor bu filtre
            # .. buradan da filtreleyebilirim
        # Wildcard
            # Boşluğa bir değer girdiğimizde , içeren, başlayan, biten , tam eşleşen
            # clear diyip iptal edebiliriz
        # Condition
            # Belirlediğimiz bir condition a göre filtreleme yapabiliriz
            # By field --> büyüktür işareti(>) --> 100k(ya da 100.000) yazalım vs vs
            # Formula kısmı daha sonra
        # Top
            # By field -- > Top 10 --> sales  --> sum --> OK
    # NOT: Filtreleme sırası: # Selection(general) --> wildcard  --> Condition --> Limit(top)
        
######################
# 4.MEASURE FILTERS
# Measurelar kullanılarak oluşturulan filtrelere denir
    # Columns : SUM(Sales)
    # Rows    : Sub-Category
    # Büyükten küçüğe sıralayalım
    # Sales ı filters kartına sürükleyelim. Bir pencere açıldı. All values ın mantığı biraz farklı, birazdan göreceğiz
        # Sum(Sum ın altındaki diğer şeyleri de seçebiliriz) --> Next
            # Range of Values
                # Min max değerleri görüyoruz. Bir aralık belirtebiliriz. Aralıktaki değerler karşıma gelecek
            # At least
                # Minimum değeri seçiyoruz. "x" değerinden büyük olanları getir
            # At most
                # Maximum değeri seçiyoruz. "x" değerinden küçük olanları getir
            # Special
                # Eğer veri setinizde Null bir değer varsa, bunları filtrelemek için kullanabiliriz
        # All values --> next
            # Range of Values
                # Burada yer alan değerler öncekine göre değişti. Önceki gibi min max değerleri değil
                # Satır bazındaki sales değerini gösteriyor. Yani verisetine bakarsam sales için tüm satırlara bakarsak
                # .. örneğin en küçük değerin 0.44 olduğunu görürüz
                # Burada aralık belirlersek, o değerlerin arasındakileri getirip onların toplamını alacak
            # At least, At most, Special ın mantığı üstteki ile aynı
                
######################
# 5.DATE FILTERS            
# Date kullanılarak oluşturulan filtrelere denir       
    # Columns : YEAR(Order Date)
    # Rows    : Sub-Category
    # Sales i marks da text kartına bırakalım. Her bir yılda sub category kırılımında satış toplamlarını görüyoruz
    # Order date i filters kartına sürükleyelim. Bir pencere açıldı.Relative date ve Range of dates i birazdan göreceğiz
        # Months(Month harici bir şey de seçebilirdik) --> Next
            # General
                # Istediğimiz ayları seçip filtreleyebiliriz
            # Condition
                # İstediğimiz condition ı verebiliriz
            # Top
        # Relative Date --> Next
            # Relative Dates
                # Açılan yerde Relative dates ve range of dates arasında geçiş yapabiliyoruz normalde
                # Altta "anchor relative to" kısmına tarih girelim 30.06.2020
                # Sonra üstten "month" seçelim --> "last" --> 1 --> apply
                # Yani 30 hazirandan 1 ay öncesine baktık
            # Range of Dates --> Next
                # Açıklaması 7-8 satır altta
            # Starting date 
                # Başlangıç tarihi belirlemek için kullanılabilir
            # Ending date
                # Bitiş tarihi belirlemek için kullanılabilir
            # Special
                # Null verileri filtrelemek için kullanılabilir
        # Range of Dates --> Next
            # Tarih aralığı belirliyoruz -- > apply
            
#################
# ÖRNEKLER
#### TOP 20 MOST SOLD CUSTOMERS
    # Columns : Sum(Sales)
    # Rows    : Customer Name
    # Büyükten küçüğe sıralayalım
    # Customer name i filter a sürükleyelim
    # Top --> by field -- > top 20 -- > apply
    
#### CUSTOMERS WHOSE NAMES START WITH "S" (Let's show sum of sales also)
    # Columns : Sum(sales)
    # Rows    : Customer Name
    # Büyükten küçüğe sıralayalım
    # Customer name i filters a sürükleyelim
    # Wildcard --> starts with -- > "S"

#### TOP 20 MOST SOLD CUSTOMERS AMONG CUSTOMERS WHOSE NAMES START WITH "S"
    # Önce S harfi ile başlayanlara bakıp sonra bunların arasından en çok satış yapılan top 20 yapacağız
    # Columns : Sum(Sales)
    # Rows    : Customer Name
    # Büyükten küçüğe sıralayalım
    # Customer name i filters a sürükleyelim
    # Wildcard --> starts with -- > "S"    
    # Top --> by field -- > top 20 -- > apply

#### AMONG THE TOP 20 MOST SOLD CUSTOMERS WHOSE NAME START WITH "S"
    # Burada da önce en çok satış yapılanlar arasından "S" harfiyle başlayanları getireceğiz
    # Burada bir problem oluşacak çünkü belli bir filtreleme sıramız vardı. Bunu "DIMENSION FILTERS"
    # .. başlığının en altındaki satırda görebiliriz. Bunu şöyle çözebiliriz. Tek bir field a göre 
    # .. filtreleme yapmak zorunda değiliz. O yüzden "Customer" ları temsil eden hem customer name
    # .. hem de Customer ID yi kullanacağız
    # Columns : Sum(Sales)
    # Rows    : Customer Name
    # Büyükten küçüğe sıralayalım
    # Customer ID yi filters a sürükleyelim
    # Top --> by field -- > top 20 -- > apply
    # Customer name i filter a sürükleyelim
    # Wildcard --> starts with -- > "S" 
    # NOT: Burada "Filtering Your Data" başlığının altında da gördüğümüz gibi önce "Ara katman filtre" yaptık 
    # .. "top N" ile daha sonra "dimensions filter" yaptık aslında

#### CUSTOMERS WHO BUY MORE THAN 125 ITEMS.(Filtre olarak measure filtresi kullanalım)
    # Columns : Sum(Quantity)
    # Rows    : Customer Name
    # Büyükten küçüğe sıralayalım
    # Quantity yi filters kartına sürükleyelim
    # Sum --> next --> At least --> 125 --> Apply

#### TOTAL SALES TOP 5 DAYS BEFORE 20 August 2018
    # Columns : Sağ tık ile Order date --> MDY(Order date)
    # Rows    : Sum(Sales)
    # Tarihlere göre line chart geldi --> bar charta çevirelim marks kısmında
    # Order date i filters a sürükleyelim
    # Relative Date -- > Next --> Anchor relative to --> 20.08.2018 --> Days--> Last --> 5 --> Apply 
    # NOT: 4 gün karşımıza geldi. Çünkü 18 august 2018 de herhangi bir işlem kaydı girilmemiş. Hata yok yani

#### CALIFORNIA STATE AMONG THE TOP 10 MOST PROFITABLE CUSTOMERS
    # Columns : SUM(Profit)
    # Rows    : Customer Name
    # Büyükten küçüğe sıralayalım
    # Customer name i filtera a sürükleyelim 
    # Top --> by field -- > top 10 -- > apply
    # State i filters a sürükleyelim
    # General --> California ya seçelim --> Apply
    
#### TOP 10 MOST PROFITABLE CUSTOMERS AMONG CUSTOMERS SHOPPING IN THE STATE OF CALIFORNIA
    # Yukardaki sorunun tam tersi ancak filtreleme sırası problemim var yine. "Filtering Your Data"
    # .. kısmında önce Ara katman filtesinden "Top N" i yapıyor sonra "Dimension" ı yapıyordu.
    # .. Peki nasıl çözeceğim? "Context Filters" ile. Yani State i context filter yaparsam eğer
    # .. "Top N" filtresinden önce işlem görecek. Aşağı bakalım şimdi
    # Columns : SUM(Profit)
    # Rows    : Customer Name
    # Büyükten küçüğe sıralayalım
    # Customer name i filtera a sürükleyelim 
    # Top --> by field -- > top 10 -- > apply
    # State i filters a sürükleyelim
    # General --> California ya seçelim --> Apply    
    # State -- > "sağ tık" --> Add to context
    # Böyle yapınca önce Californiadakileri filtreledi daha sonra onların arasından 10 kişiyi buldu
    # Filters daki State de griye döndü buradan state in context filter olduğunu anlayabiliyorum
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
