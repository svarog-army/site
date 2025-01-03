interface DragScrollOptions {
    scrollSpeed?: number;
    activeClass?: string;
}
interface DragScrollResult {
    destroy: () => void;
}
declare function createDragScroll(selector: string, options?: DragScrollOptions): DragScrollResult;
declare const vacancyGallery: DragScrollResult;
