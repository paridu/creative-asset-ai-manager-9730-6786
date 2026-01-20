"use client";

import { Header } from "@/components/Header";
import { AssetCard } from "@/components/AssetCard";
import { MOCK_ASSETS } from "@/constants/mockData";
import { useState } from "react";
import { FilterCategory } from "@/types/asset";

export default function Dashboard() {
  const [activeFilter, setActiveFilter] = useState<FilterCategory>('all');

  const filters: { label: string; value: FilterCategory }[] = [
    { label: "All Assets", value: "all" },
    { label: "Images", value: "image" },
    { label: "Vectors", value: "vector" },
    { label: "Documents", value: "document" },
  ];

  return (
    <>
      <Header />
      <div className="flex-1 overflow-y-auto p-6">
        <div className="mb-8">
          <h1 className="text-2xl font-bold mb-4">Library</h1>
          <div className="flex gap-2">
            {filters.map((f) => (
              <button
                key={f.value}
                onClick={() => setActiveFilter(f.value)}
                className={`px-4 py-1.5 rounded-full text-xs font-medium transition-all ${
                  activeFilter === f.value 
                  ? "bg-white text-black" 
                  : "bg-zinc-900 text-zinc-400 hover:bg-zinc-800"
                }`}
              >
                {f.label}
              </button>
            ))}
          </div>
        </div>

        <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5 gap-6">
          {MOCK_ASSETS.map((asset) => (
            <AssetCard key={asset.id} asset={asset} />
          ))}
          
          {/* Empty State/Upload Placeholder */}
          <div className="border-2 border-dashed border-zinc-800 rounded-xl flex flex-col items-center justify-center aspect-[4/3] hover:border-zinc-700 transition-colors cursor-pointer group">
            <div className="w-10 h-10 rounded-full bg-zinc-900 flex items-center justify-center mb-2 group-hover:scale-110 transition-transform">
              <span className="text-zinc-500 text-xl">+</span>
            </div>
            <p className="text-[10px] text-zinc-500 font-medium">Drop to add assets</p>
          </div>
        </div>
      </div>
    </>
  );
}