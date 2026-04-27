import { useTranslation } from 'react-i18next'

export default function Technologies() {
  const { t } = useTranslation()
  return (
    <div
      className="w-full h-full bg-cover bg-right sm:bg-center bg-no-repeat relative"
      style={{
        backgroundImage:
          "image-set(url('/img/technologies.webp') type('image/webp'), url('/img/technologies.png') type('image/png'))",
      }}
    >
      <div className="absolute inset-0 bg-black/50 z-0" />
      <div className="flex flex-col justify-center gap-5 items-center py-[233px] mx-auto">
        <h2 className="text-4xl md:text-6xl text-center uppercase z-10 text-[--main-grey]">
          {t('technologies.title')}
        </h2>
        <p className="text-xl text-center max-w-[850px] px-4 z-10 text-[--main-grey]">
          {t('technologies.description')}
        </p>
      </div>
    </div>
  )
}
