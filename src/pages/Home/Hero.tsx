import { useTranslation } from 'react-i18next'
import { LINKS } from '../../config'
import JoinButton from '../../components/JoinButton'

export default function Hero() {
  const { t } = useTranslation()
  return (
    <div className="flex flex-col justify-center bg-black min-h-screen sm:h-screen w-full bg-cover bg-right sm:bg-center">
      <div className="container mx-auto lg:mx-auto px-5 lg:px-16 mt-36 md:mt-0">
        <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-4 items-start">
          <div className="flex h-[180px] md:h-[400px] col-span-1 order-1">
            <img className="h-full object-cover mx-auto" src="/img/svarog-logo.svg" alt="Svarog logo" />
          </div>
          <div className="flex flex-col items-center md:items-start mb-10 order-2 col-span-1 xl:col-span-2">
            <h1 className="text-[--main-grey] text-center md:text-start uppercase font-bold text-2xl lg:text-4xl lg:leading-[40px]">
              {t('hero.susb')}
            </h1>
            <span className="text-[--main-grey] mb-5 mx-auto md:mx-0 uppercase text-5xl lg:text-[48px] xl:text-[96px] font-ethnocentric">
              {t('hero.svarog')}
            </span>
            <p className="leading-5 lg:text-xl text-center md:text-start text-[--main-white-87] mb-10 px-5 md:px-0">
              {t('hero.description')}
            </p>

            <div className="w-full flex flex-col justify-start xl:flex-row items-start">
              <div className="mx-auto md:mx-0">
                <JoinButton />
              </div>
              <a
                href={LINKS.testDrive}
                target="_blank"
                rel="noreferrer"
                className="mx-auto md:mx-0 mt-12 xl:mt-0 xl:ms-12 text-[--main-green] py-4 uppercase underline hover:text-[--main-white-87] focus:text-[--main-white-87] active:no-underline"
              >
                {t('hero.signUpTestDrive')}
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}
