from app import env as env


def render_client(title, client, style, form, table, qrcode):
	template = env.get_template('layout.html')
	s = template.render(title=title, cl=client, style=style, form=form, table=table, qrcode=qrcode)
	return s
