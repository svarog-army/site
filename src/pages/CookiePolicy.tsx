import { useTranslation } from 'react-i18next'

export default function CookiePolicy() {
  const { t } = useTranslation()
  return (
    <section className="lg:px-16 pt-32 flex flex-col gap-4 container mx-auto py-20 lg:min-h-[calc(100vh-288px)]">
      <h1 className="text-4xl font-semibold pb-5">{t('cookiePolicy.title')}</h1>
      <p><strong>{t('cookiePolicy.intro')}</strong></p>

      <p><strong>{t('cookiePolicy.section1Title')}</strong></p>
      <p>{t('cookiePolicy.section1')}</p>

      <p><strong>{t('cookiePolicy.section2Title')}</strong></p>
      <p>{t('cookiePolicy.section2')}</p>

      <p><strong>{t('cookiePolicy.section3Title')}</strong></p>
      <ul className="list-disc ml-6">
        <li>
          <em>{t('cookiePolicy.section3aLabel')}</em>: {t('cookiePolicy.section3aText')}
        </li>
        <li>
          <em>{t('cookiePolicy.section3bLabel')}</em>: {t('cookiePolicy.section3bText')}
        </li>
      </ul>

      <p><strong>{t('cookiePolicy.section4Title')}</strong></p>
      <p>{t('cookiePolicy.section4')}</p>

      <p><strong>{t('cookiePolicy.section5Title')}</strong></p>
      <p>{t('cookiePolicy.section5')}</p>

      <p><strong>{t('cookiePolicy.section6Title')}</strong></p>
      <p>{t('cookiePolicy.section6')}</p>

      <p>{t('cookiePolicy.thank')}</p>
    </section>
  )
}
