import { useTranslation } from 'react-i18next'
import { Link } from 'react-router-dom'
import { LINKS } from '../config'

export default function Footer() {
  const { t, i18n } = useTranslation()

  return (
    <div className="w-full h-full bg-black pt-[70px]">
      <div className="container mx-auto px-0 md:px-5 lg:px-10 xl:px-16">
        <div className="flex flex-col md:flex-row justify-center w-full">
          <div className="w-[100%]">
            <div className="mb-[30px] md:h-[80px] flex flex-col md:flex-row md:justify-between">
              <div className="flex flex-col md:flex-row md:me-auto">
                <div className="max-w-[140px] mx-auto md:mx-0 mb-2 md:mb-0">
                  <img className="w-[90px] h-[90px] object-cover mx-auto" src="/img/svarog-logo.svg" alt="Svarog logo" />
                </div>
                <div className="flex flex-row md:flex-col justify-center mb-12 md:mb-0">
                  <p className="text-[--main-grey] text-center text-base md:text-start w-[220px]">
                    {t('footer.unitName')}
                  </p>
                </div>
              </div>

              <div className="flex flex-row justify-between mx-auto md:mx-0 w-[320px] md:w-auto">
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

                <div className="flex ms-14 my-auto">
                  <select
                    value={i18n.language}
                    onChange={(e) => i18n.changeLanguage(e.target.value)}
                    className="block py-2.5 px-0 w-full text-sm text-[--main-grey] bg-transparent border-none appearance-none focus:outline-none cursor-pointer"
                  >
                    <option className="text-black text-center" value="uk">УКР</option>
                    <option className="text-black text-center" value="en">EN</option>
                  </select>
                </div>
              </div>
            </div>

            <div className="mb-[30px] text-start md:text-end pe-7 w-[320px] md:w-full mx-auto md:mx-0 flex gap-4 justify-start md:justify-end">
              <Link to="/cookie-policy" className="text-slate-600 text-sm hover:text-slate-400 transition">
                Cookie policy
              </Link>
              <Link to="/privacy-policy" className="text-slate-600 text-sm hover:text-slate-400 transition">
                {t('privacyPolicy.title')}
              </Link>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}
