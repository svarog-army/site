import { useTranslation } from 'react-i18next'
import { LINKS } from '../../config'

export default function Vacancies() {
  const { t } = useTranslation()
  const list = t('vacancies.list', { returnObjects: true }) as string[]

  return (
    <div id="vacancies" className="w-full h-full pt-[90px] bg-[--main-black]">
      <div className="container mx-auto px-2 lg:px-10 xl:px-16 bg-no-repeat">
        <div className="sm:max-w-96 md:max-w-full mx-auto flex flex-col justify-between gap-6">
          <h2 className="text-4xl md:text-6xl text-[--main-grey-87] text-center mb-5">
            {t('vacancies.title')}
          </h2>

          {/* Desktop grid */}
          <div className="hidden md:flex flex-row flex-wrap gap-5 justify-center">
            {list.map((name, i) => (
              <div
                key={i}
                className="w-[250px] h-[140px] border border-[--main-grey] text-center flex flex-col justify-center"
              >
                <span className="text-[--main-white-87] text-xl font-semibold">{name}</span>
              </div>
            ))}
          </div>

          {/* Mobile list */}
          <div className="flex md:hidden flex-col">
            <ul className="list-disc pl-5">
              {list.map((name, i) => (
                <li key={i} className="text-[--main-white-87] text-xl">{name}</li>
              ))}
            </ul>
          </div>
        </div>

        <div className="flex justify-center pt-[90px] pb-[120px]">
          <a
            href={LINKS.joinForm}
            target="_blank"
            rel="noreferrer"
            className="relative inline-flex items-center justify-start py-3 px-12 overflow-hidden font-semibold text-white transition-all duration-150 ease-in-out bg-[--main-grey-opacity] group"
          >
            <span className="absolute bottom-0 left-0 w-full h-1 transition-all duration-150 ease-in-out bg-[--main-green] group-hover:h-full" />
            <span className="absolute bottom-0 left-0 w-full h-1 transition-all duration-150 ease-in-out bg-[--main-green] group-hover:bg-[--main-grey]" />
            <span className="relative w-full text-center text-base text-[--main-white-87] transition-colors duration-200 ease-in-out group-hover:text-black">
              {t('vacancies.submitApplication')}
            </span>
          </a>
        </div>
      </div>
    </div>
  )
}
