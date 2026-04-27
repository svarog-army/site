import { useTranslation } from 'react-i18next'

export default function AboutUs() {
  const { t } = useTranslation()
  return (
    <div
      className="w-full h-full bg-cover bg-center bg-no-repeat"
      style={{
        backgroundImage:
          "image-set(url('/img/about-us/about-us.webp') type('image/webp'), url('/img/about-us/about-us.jpg') type('image/jpeg'))",
      }}
    >
      <div className="container mx-auto pt-[500px] pb-[100px] px-2 lg:px-10 xl:px-16 bg-no-repeat">
        <div className="flex flex-col justify-between gap-6 max-w-[900px]">
          <h2 className="text-4xl md:text-6xl text-[--main-grey] text-start mb-5">
            {t('aboutUs.title')}
          </h2>
          <p className="text-lg text-start text-[--main-grey]">
            {t('aboutUs.description')}
          </p>
        </div>
      </div>
    </div>
  )
}
