import { useState } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import { useTranslation } from 'react-i18next'
import { LINKS } from '../config'

export default function Header() {
  const { t, i18n } = useTranslation()
  const [menuOpen, setMenuOpen] = useState(false)
  const navigate = useNavigate()

  function changeLanguage(lang: string) {
    i18n.changeLanguage(lang)
  }

  function goToVacancies() {
    setMenuOpen(false)
    navigate('/?scroll=vacancies')
    setTimeout(() => {
      document.getElementById('vacancies')?.scrollIntoView({ behavior: 'smooth' })
    }, 100)
  }

  return (
    <>
      <div className="flex justify-center">
        <div className="container absolute flex justify-between items-center w-full px-5 lg:px-16 mt-5 md:mt-12 text-black z-40">
          <Link to="/" className="flex items-start h-[24px]">
            <img className="h-full object-cover" src="/img/svarog-logo.svg" alt="Svarog logo" />
            <span className="text-xl font-bold font_uaf_bold ml-2 text-[--main-grey-87]">424</span>
            <span className="text-xl font-bold font_uaf_bold ml-2 text-[--main-grey] hidden sm:inline uppercase">
              Svarog
            </span>
          </Link>

          <div className="hidden lg:inline-flex">
            <Link to="/" className="text-[--main-white-87] text-base px-[10px] py-3 hover:bg-[--main-grey-opacity]">
              {t('nav.main')}
            </Link>
            <a
              href={LINKS.testDrive}
              target="_blank"
              rel="noreferrer"
              className="text-[--main-white-87] text-base px-[10px] py-3 hover:bg-[--main-grey-opacity]"
            >
              {t('nav.testCourse')}
            </a>
            <Link to="/donate" className="text-[--main-white-87] text-base px-[10px] py-3 hover:bg-[--main-grey-opacity]">
              {t('nav.toSupport')}
            </Link>
            <button
              onClick={goToVacancies}
              className="text-[--main-white-87] text-base px-[10px] py-3 hover:bg-[--main-grey-opacity] cursor-pointer"
            >
              {t('nav.vacancies')}
            </button>
          </div>

          <div className="flex items-center gap-4 h-[24px]">
            <div className="flex gap-3">
              <a href={LINKS.telegram} target="_blank" rel="noreferrer" className="my-auto">
                <img src="/img/telegram.svg" width="24" height="24" alt="Telegram" className="hover:scale-110 active:opacity-50 transition" />
              </a>
              <a href={LINKS.instagram} target="_blank" rel="noreferrer" className="my-auto">
                <img src="/img/instagram.svg" width="24" height="24" alt="Instagram" className="hover:scale-110 active:opacity-50 transition" />
              </a>
              <a href={LINKS.facebook} target="_blank" rel="noreferrer" className="my-auto">
                <img src="/img/facebook.svg" width="24" height="24" alt="Facebook" className="hover:scale-110 active:opacity-50 transition" />
              </a>
            </div>

            <button className="py-1 lg:hidden" onClick={() => setMenuOpen(true)} aria-label={t('nav.openMenu')}>
              <img src="/img/burger.svg" width="26" height="26" alt={t('nav.openMenu')} className="hover:scale-110 active:opacity-50 transition" />
            </button>

            <div className="hidden lg:flex gap-8">
              <select
                value={i18n.language}
                onChange={(e) => changeLanguage(e.target.value)}
                className="block py-2.5 px-0 w-full text-sm text-[--main-grey] bg-transparent border-none appearance-none focus:outline-none cursor-pointer"
              >
                <option className="text-black text-center" value="uk">УКР</option>
                <option className="text-black text-center" value="en">EN</option>
              </select>
            </div>
          </div>
        </div>
      </div>

      {/* Mobile sidebar */}
      <div
        className={`fixed z-50 inset-y-0 right-0 w-full bg-[--main-grey] transform transition-transform duration-300 ease-in-out ${
          menuOpen ? 'translate-x-0' : 'translate-x-full'
        }`}
      >
        <button
          className="absolute top-8 right-8 py-1 text-[--main-black]"
          onClick={() => setMenuOpen(false)}
          aria-label={t('nav.closeMenu')}
        >
          <img src="/img/cross.svg" width="32" height="32" alt={t('nav.closeMenu')} className="hover:scale-110 active:opacity-50 transition" />
        </button>

        <div className="flex flex-col mt-40 space-y-4 text-end pe-8">
          <Link to="/" onClick={() => setMenuOpen(false)} className="text-[--menu-black] text-3xl font-semibold hover:underline active:no-underline">
            {t('nav.main')}
          </Link>
          <a href={LINKS.testDrive} target="_blank" rel="noreferrer" onClick={() => setMenuOpen(false)} className="text-[--menu-black] text-3xl font-semibold hover:underline active:no-underline">
            {t('nav.testCourse')}
          </a>
          <Link to="/donate" onClick={() => setMenuOpen(false)} className="text-[--menu-black] text-3xl font-semibold hover:underline active:no-underline">
            {t('nav.toSupport')}
          </Link>
          <button onClick={goToVacancies} className="text-[--menu-black] text-3xl font-semibold hover:underline active:no-underline text-end">
            {t('nav.vacancies')}
          </button>
        </div>

        <div className="flex flex-col mt-20 space-y-4 text-end pe-8">
          <span className="text-2xl text-[--menu-black]">{t('nav.changeLanguage')}</span>
          <select
            value={i18n.language}
            onChange={(e) => { changeLanguage(e.target.value); setMenuOpen(false) }}
            className="ms-auto py-2.5 px-0 pe-0 text-3xl text-[--menu-black] bg-transparent border-none appearance-none focus:outline-none cursor-pointer"
          >
            <option value="uk">Українська</option>
            <option value="en">English</option>
          </select>
        </div>
      </div>
    </>
  )
}
