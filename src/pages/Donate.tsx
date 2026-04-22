import { useTranslation } from 'react-i18next'
import SupportButton from '../components/SupportButton'

export default function Donate() {
  const { t } = useTranslation()
  return (
    <div className="flex flex-col justify-center bg-black w-full bg-cover bg-right sm:bg-center mt-4">
      <div className="container mx-auto lg:mx-auto px-5 lg:px-16 mt-36">
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4 xl:gap-5 items-start">
          <div className="hidden md:flex max-h-[470px] max-w-[470px] col-span-1 order-1">
            <img className="h-full object-cover mx-auto" src="/img/pic.svg" alt="Svarog logo" />
          </div>
          <div className="flex flex-col items-center md:items-start sm:ms-6 mb-10 order-2 col-span-1">
            <h1 className="text-[--main-grey] text-center md:text-start font-sans uppercase text-4xl sm:text-5xl lg:text-6xl lg:leading-[40px]">
              {t('donate.title')}
            </h1>
            <span className="text-[--main-grey] mb-5 mt-1 mx-auto md:mx-0 uppercase text-4xl sm:text-5xl lg:text-6xl font-sans font-bold">
              {t('donate.subtitle')}
            </span>
            <p className="leading-5 lg:text-xl text-base md:text-xl text-center md:text-start text-[--main-white-87] mb-10 px-5 md:px-0">
              {t('donate.description')}
            </p>
            <div className="mx-auto md:mx-0">
              <SupportButton />
            </div>
          </div>
          <div className="flex md:hidden max-h-[470px] max-w-[470px] col-span-1 order-3 mx-auto text-center">
            <img className="h-full object-cover" src="/img/pic.svg" alt="Svarog logo" />
          </div>
        </div>
      </div>
    </div>
  )
}
