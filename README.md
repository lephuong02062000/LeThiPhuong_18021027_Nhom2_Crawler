# 
- start_urls chứa các link bắt đầu lấy, cụ thể ở đây link bắt đầu crawl là link danh mục chứa các link bài báo
- Hàm parse:
	+ response lúc này chính là nội dung được trả về khi truy cập từng link trong start_urls.
	+ response.css() cho phép lựa chọn phần tử html sử dụng CSS.
	+ links_article = response.css('h3.title-news a::attr(href)').getall() trả về danh sách các link bài báo trong link danh mục hiện tại 
	+ yield scrapy.Request(link_article, callback=self.get) với mỗi link bài báo  tạo một request mới tới link bài báo này, tham số callback xác định hàm sẽ thực hiện sau khi response được trả về. Ở đây là hàm get
Trong một danh mục sẽ chia ra nhiều page vì link bài báo có số lượng lớn:
	+ next_page = response.css('a.next-page::attr(href)').get() trả về link page tiếp theo trong cùng 1 danh mục 
	+ next_page = response.urljoin(next_page) xây dựng một cách đầy đủ link liên kết vì có những link chỉ mang tính tương đối
	+ yield scrapy.Request(next_page, callback=self.parse) với link page tiếp theo ta lại tạo một request tới link page tiếp theo này , và gọi lại chính hàm parse để thực hiện tương tự như link danh mục đầu tiên
- Hàm get:
	+ response lúc này chính là nội dung được trả về khi truy cập link ở hàm parse mà response.css('h3.title-news a::attr(href)').getall() trả về cũng chính là link dẫn đến bài báo 
	+ title = response.css('h1.title-detail::text').get() trả về title bài báo 
	+ category = response.css('ul.breadcrumb li a::text').get() trả về danh mục chứa bài báo 
	+ update = response.css('span.date::text').get()trả về ngày update bài báo 
	+ link_page = response.url trả về link bài báo
	+ description = response.css('p.description::text').get() trả về mô tả của bài báo 

	+ for i in response.css('article.fck_detail p.Normal'):
    		content = ''.join(i.css('*::text').getall())
	trả về đầy đủ nội dung của bài viết

	+ image_link = response.css('div.fig-picture img::attr(data-src)').get() trả về link ảnh trong bài viết

	+ image_description = response.css('div.fig-picture img::attr(alt)').get() trả về mô tả của link ảnh trong bài báo 

	+ author = response.css('p.author_mail strong::text').get()
	trả về tác giả của bài báo 

	+ key_words = response.css('meta[name="keywords"]::attr("content")').get() trả về những keyword của bài báo

	+ tags = response.css('meta[name="its_tag"]::attr("content")').get()trả về các tag của bài báo 
	







