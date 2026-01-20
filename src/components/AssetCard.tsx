import { Asset } from "@/types/asset";
import { Maximize2, MoreHorizontal } from "lucide-react";

export const AssetCard = ({ asset }: { asset: Asset }) => {
  return (
    <div className="group relative bg-zinc-900 rounded-xl overflow-hidden border border-zinc-800 hover:border-accent/50 transition-all">
      <div className="aspect-[4/3] overflow-hidden bg-zinc-800 relative">
        <img 
          src={asset.thumbnail_url} 
          alt={asset.filename}
          className="w-full h-full object-cover transition-transform duration-300 group-hover:scale-105"
        />
        <div className="absolute inset-0 bg-black/40 opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center gap-2">
          <button className="p-2 bg-white/10 backdrop-blur-md rounded-full text-white hover:bg-white/20">
            <Maximize2 size={18} />
          </button>
        </div>
      </div>
      
      <div className="p-3">
        <div className="flex items-start justify-between mb-1">
          <h3 className="text-xs font-medium text-zinc-200 truncate pr-4">{asset.filename}</h3>
          <button className="text-zinc-500 hover:text-zinc-300">
            <MoreHorizontal size={16} />
          </button>
        </div>
        
        <div className="flex flex-wrap gap-1 mt-2">
          {asset.tags.slice(0, 2).map(tag => (
            <span key={tag} className="text-[10px] bg-zinc-800 text-zinc-400 px-1.5 py-0.5 rounded">
              #{tag}
            </span>
          ))}
          {asset.tags.length > 2 && (
            <span className="text-[10px] text-zinc-500 px-1 py-0.5">+{asset.tags.length - 2}</span>
          )}
        </div>
      </div>
    </div>
  );
};