import { Search, SlidersHorizontal, Plus } from "lucide-react";

export const Header = () => {
  return (
    <header className="h-16 border-b border-zinc-800 flex items-center justify-between px-6 bg-background/80 backdrop-blur-md sticky top-0 z-10">
      <div className="flex-1 max-w-2xl relative">
        <Search className="absolute left-3 top-1/2 -translate-y-1/2 text-zinc-500" size={18} />
        <input 
          type="text" 
          placeholder='Search by name, "vibe", or color...'
          className="w-full bg-zinc-900 border border-zinc-800 rounded-full py-2 pl-10 pr-4 text-sm focus:outline-none focus:border-accent transition-colors"
        />
      </div>
      
      <div className="flex items-center gap-4 ml-4">
        <button className="flex items-center gap-2 text-zinc-400 hover:text-white text-sm px-3 py-2 border border-zinc-800 rounded-md transition-colors">
          <SlidersHorizontal size={16} />
          <span>Filters</span>
        </button>
        <button className="bg-accent hover:bg-blue-600 text-white p-2 rounded-full transition-colors">
          <Plus size={20} />
        </button>
      </div>
    </header>
  );
};