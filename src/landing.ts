interface DragScrollOptions {
  scrollSpeed?: number;
  activeClass?: string;
}

interface DragScrollResult {
  destroy: () => void;
}

function createDragScroll(
  selector: string,
  options: DragScrollOptions = {},
): DragScrollResult {
  const slider = document.querySelector(selector) as HTMLElement;
  if (!slider) {
    throw new Error(`Element with selector "${selector}" not found`);
  }

  let isDown = false;
  let startX: number;
  let scrollLeft: number;

  const defaultOptions: Required<DragScrollOptions> = {
    scrollSpeed: 3,
    activeClass: 'active',
  };

  const settings: Required<DragScrollOptions> = {...defaultOptions, ...options};

  function handleMouseDown(e: MouseEvent): void {
    isDown = true;
    slider.classList.add(settings.activeClass);
    startX = e.pageX - slider.offsetLeft;
    scrollLeft = slider.scrollLeft;
  }

  function handleMouseLeave(): void {
    isDown = false;
    slider.classList.remove(settings.activeClass);
  }

  function handleMouseUp(): void {
    isDown = false;
    slider.classList.remove(settings.activeClass);
  }

  function handleMouseMove(e: MouseEvent): void {
    if (!isDown) return;
    e.preventDefault();
    const x = e.pageX - slider.offsetLeft;
    const walk = (x - startX) * settings.scrollSpeed;
    slider.scrollLeft = scrollLeft - walk;
  }

  function addEventListeners(): void {
    slider.addEventListener('mousedown', handleMouseDown);
    slider.addEventListener('mouseleave', handleMouseLeave);
    slider.addEventListener('mouseup', handleMouseUp);
    slider.addEventListener('mousemove', handleMouseMove);
  }

  function removeEventListeners(): void {
    slider.removeEventListener('mousedown', handleMouseDown);
    slider.removeEventListener('mouseleave', handleMouseLeave);
    slider.removeEventListener('mouseup', handleMouseUp);
    slider.removeEventListener('mousemove', handleMouseMove);
  }

  addEventListeners();

  return {
    destroy: removeEventListeners,
  };
}

const vacancyGallery = createDragScroll('.vacancy-gallery', {scrollSpeed: 3});
