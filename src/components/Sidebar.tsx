import { LayoutDashboard, Image as ImageIcon, FolderCanvas, Settings, Clock, Zap } from "lucide-react";

export const Sidebar = () => {
  const menuItems = [
    { icon: LayoutDashboard, label: "All Assets", active: true },
    { icon: Clock, label: "Recent" },
    { icon: FolderCanvas, label: "Projects" },
    { icon: Zap, label: "AI Collections" },
  ];

  return (
    <aside className="w-64 border-r border-zinc-800 h-screen hidden md:flex flex-col p-4 bg-background">
      <div className="flex items-center gap-2 px-2 mb-8">
        <div className="w-8 h-8 bg-accent rounded-lg flex items-center justify-center font-bold text-white">O</div>
        <span className="font-bold text-xl tracking-tight">OVERLORD</span>
      </div>
      
      <nav className="flex-1 space-y-1">
        {menuItems.map((item) => (
          <button
            key={item.label}
            className={`w-full flex items-center gap-3 px-3 py-2 rounded-md transition-colors ${
              item.active ? "bg-zinc-800 text-white" : "text-zinc-400 hover:bg-zinc-900 hover:text-zinc-200"
            }`}
          >
            <item.icon size={18} />
            <span className="text-sm font-medium">{item.label}</span>
          </button>
        ))}
      </nav>

      <div className="border-t border-zinc-800 pt-4">
        <button className="w-full flex items-center gap-3 px-3 py-2 text-zinc-400 hover:text-white transition-colors">
          <Settings size={18} />
          <span className="text-sm font-medium">Settings</span>
        </button>
      </div>
    </aside>
  );
};