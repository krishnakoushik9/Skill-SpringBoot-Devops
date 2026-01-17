
# Shiva Temple Game – Unreal Engine 5.6 Design Notes

## Concept Overview
- **Game Length**: Around 30 minutes  
- **Final Scene**: Shiva Temple  
- **Main Enemy Type**: Skeleton soldiers (red glowing eyes, old-school soldier look with capes)  
- **Boss Fight**: Wave 1, Wave 2, Final Boss (TBD)  

---

## Village and Bazaar Sequence
- **Location**: Small village with a marketplace (bazaar)  
- **Details**:
  - Villagers: UE mannequins with animations  
  - Ambient Sound: Soft, melodious temple/bazaar music  
  - Artifacts and simple props around  

### Panic System
- **Animation Pack**: Mob-Scared pack  
- **Trigger**:
  - Player draws sword  
  - Skeleton soldiers walk toward the player  
  - Nearby villagers (mannequins) react with panic animations  
  - Panic sound effect (e.g., `scared.mp3`) triggered simultaneously  

---

## Combat System
- **Mechanics**: Simple melee combat  
- **Tools**:
  - Sword drawing triggers combat mode  
  - Uses animation montages  
  - Root motion recommended for smoother transitions  

### Combat Phases
- Wave 1: Initial group of skeleton soldiers  
- Wave 2: After exiting the village to a semi-urban area  
- Final Boss: At Shiva Temple (character model TBD)  

### Recommended Tutorials
- [UE5.6 Melee Combat - Part 7 Series](https://www.youtube.com/watch?v=khOZpVlmFOM)
- [How To Make Melee Combat System In UE5](https://www.youtube.com/watch?v=iPfU1SmzkkY)

---

## Sound & Music Transitions
- **Bazaar Ambient**:
  - Play on level start  
  - Includes ambient sounds, bells, calm market vibe  

- **Combat Trigger**:
  - Draw sword → fade out ambient → fade in combat music  
  - Add intense "tap-tap-tap" fight music  

- **Post-Combat**:
  - Music fades after wave ends  
  - Reset or switch music if new wave begins  

---

## Horse Riding to Shiva Temple
- **Trigger**: After exiting bazaar, offer a horse  
- **Horse Setup**:
  - Create mount/dismount function  
  - Attach player to saddle socket  
  - Control override while riding  

### Recommended Tutorials
- [UE5 Horse Riding Tutorial](https://www.youtube.com/watch?v=y-rDnRmUCtk)
- [Mounting Horse in UE5](https://www.youtube.com/watch?v=-hU6RvUNGV8)

---

## Visual & Vibe Details
- **Skeleton Soldiers**:
  - Red glowing eyes  
  - Capes and historic military outfits  

- **Lighting**:
  - Mix dusk lighting with mystical glow effects  
  - Use Global Illumination tweaks (still WIP)  

- **NPC Details**:
  - Blend states and trigger animation montages based on player action  

---

## Assets & Tools to Explore
- Mob Scared Animation Pack  
- 3D Marketplace for Final Boss model  
- Combat animation packs  
- Audio cue systems  
- Horse riding plugins or blueprints  

---

## To-Do List
- [ ] Implement basic melee combat  
- [ ] Add skeleton soldier enemy class with red eyes and capes  
- [ ] Apply panic animation and sound to NPCs  
- [ ] Set ambient and combat music transitions  
- [ ] Create basic mount/dismount horse blueprint  
- [ ] Finalize wave structure and boss model  
- [ ] Polish Global Illumination and lighting effects  