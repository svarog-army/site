import { useTranslation } from 'react-i18next'

const weapons = [
  { key: 'fpv', img: '/img/choose-weapon/fpv-drone.jpg' },
  { key: 'aerialRecon', img: '/img/choose-weapon/rozvid-krilo.jpg' },
  { key: 'heavyBombers', img: '/img/choose-weapon/bomber.jpg' },
  { key: 'impactWing', img: '/img/choose-weapon/udar-krilo.jpg' },
] as const

export default function ChooseWeapon() {
  const { t } = useTranslation()
  return (
    <div className="container mx-auto pb-20 px-2 lg:px-10 xl:px-16 pt-[90px]">
      <h2 className="text-4xl md:text-6xl text-center uppercase text-[--main-grey-87] mb-[70px]">
        {t('chooseWeapon.title')}
      </h2>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-10 desktop:justify-start">
        {weapons.map(({ key, img }) => (
          <div key={key} className="px-2 md:px-0">
            <div className="h-[250px]">
              <img className="h-full object-cover mx-auto w-full" src={img} alt={t(`chooseWeapon.${key}.name`)} />
            </div>
            <div className="flex flex-col justify-center py-3 mx-auto">
              <span className="text-4xl text-start mt-5 mb-4 uppercase z-10 text-[--main-grey-87]">
                {t(`chooseWeapon.${key}.name`)}
              </span>
              <p className="text-xl text-start max-w-[850px] z-10 text-[--main-white-87]">
                {t(`chooseWeapon.${key}.description`)}
              </p>
            </div>
          </div>
        ))}
      </div>
    </div>
  )
}
