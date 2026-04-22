import { useTranslation } from 'react-i18next'

interface Section {
  heading?: string
  paragraphs: string[]
}

export default function PrivacyPolicy() {
  const { t, i18n } = useTranslation()
  const sections = t('privacyPolicy.sections', { returnObjects: true }) as Section[]
  const ukOnlySections = t('privacyPolicy.sectionsUkOnly', { returnObjects: true }) as Section[]
  const isUk = i18n.language === 'uk'

  return (
    <section className="px-6 lg:px-16 pt-32 flex flex-col gap-4 container mx-auto py-20 min-h-[calc(100vh-288px)]">
      <h1 className="text-4xl font-semibold pb-5">{t('privacyPolicy.title')}</h1>

      {sections.map((section, i) => (
        <div key={i}>
          {section.heading && (
            <ol start={i + 1} className="list-decimal">
              <li>{section.heading.replace(/^\d+\.\s*/, '')}</li>
            </ol>
          )}
          {section.paragraphs.map((p, j) => (
            <p key={j}>{p}</p>
          ))}
        </div>
      ))}

      {isUk && ukOnlySections.map((section, i) => (
        <div key={`uk-${i}`}>
          {section.heading && (
            <ol start={9 + i} className="list-decimal">
              <li>{section.heading.replace(/^\d+\.\s*/, '')}</li>
            </ol>
          )}
          {section.paragraphs.map((p, j) => (
            <p key={j}>{p}</p>
          ))}
        </div>
      ))}
    </section>
  )
}
