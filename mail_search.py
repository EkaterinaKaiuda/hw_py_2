from selene import browser, be, have


browser.open('https://ya.ru')
browser.element('[name="text"]').should(be.blank).type('blablabla2').press_enter()
browser.element('[id="search-result"]').should(have.no.text('pupupuuu2'))
