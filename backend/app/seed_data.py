import json
from typing import List, Dict, Any

SEED_CASES: List[Dict[str, Any]] = [
    {
        "id": "arjuna-dilemma",
        "title": "Arjuna's Dilemma on the Threshold of War",
        "subtitle": "Attachment, Moral Paralysis, and the Fracture of Duty at Kurukshetra",
        "parva": "Bhishma Parva",
        "chapter_reference": "Mahābhārata VI.23–VI.40 / Bhagavad Gītā Ch. 1–2",
        "characters": ["Arjuna", "Krishna", "Bhishma", "Drona", "Yudhishthira"],
        "category": "Duty vs Attachment",
        "strategic_themes": ["Crisis Leadership", "Consequence Analysis", "Deontology vs Consequentialism", "Role Responsibility"],
        "ethical_themes": ["Svadharma (Personal Duty)", "Karuna (Compassion)", "Kula-dharma (Family Order)", "Moral Injury"],
        "difficulty": "Foundational",
        "estimated_time": "12-15 min",
        "order_index": 1,
        "context": (
            "The conches have sounded on Kurukshetra. Two colossal armies stand poised for catastrophic conflict. "
            "Arjuna, the greatest warrior of the Pandavas, requests his charioteer Krishna to draw up between both lines. "
            "Gazing across the field, he does not see abstract enemies; he sees his grandsire Bhishma who bounced him on his knee, "
            "his preceptor Drona who trained his hand to loose an arrow, uncles, cousins, childhood companions, and sons. "
            "His limbs tremble, his bow Gandiva slips from his grasp, and a profound crisis engulfs him: how can righteous sovereignty "
            "be purchased at the price of exterminating the very lineage and mentors who gave life meaning?"
        ),
        "dilemma": (
            "Should Arjuna execute his social and military duty as a Kshatriya warrior to eliminate unrighteousness (Adharma) "
            "and establish justice for his kingdom, even when it demands killing his venerable elders, beloved kin, and risking "
            "the moral collapse of familial society? Or should he renounce the fight, embrace ascetic renunciation or exile, and refuse bloodshed?"
        ),
        "why_difficult": (
            "This dilemma cannot be solved by a simple moral homily. On one side stands deontology and public duty: "
            "the Kaurava regime has systematically dismantled justice (the disrobing of Draupadi, deceitful dice matches, refusing five villages). "
            "If the Pandavas walk away, impunity is normalized across the subcontinent. On the other side stands genuine consequentialist horror: "
            "the war will slaughter millions, annihilate family lineages, and inflict irreparable trauma upon civil society. "
            "Arjuna is trapped between committing what feels like patricide/fratricide and abandoning his solemn obligation as protector of Dharma."
        ),
        "stakeholders": [
            {
                "name": "Arjuna (The Decision-Maker)",
                "role": "Chief Pandava Champion & Kshatriya Warrior",
                "interests": "Maintaining moral self-respect, avoiding the sin of slaying mentors, escaping soul-crushing grief.",
                "risks": "Moral injury, eternal remorse, being branded a coward if he retreats; psychological devastation if he fights.",
                "expectations": "To lead the vanguard to victory, yet yearning for ethical peace of mind.",
                "icon_name": "shield"
            },
            {
                "name": "Bhishma & Drona (The Elders on the Kaurava Line)",
                "role": "Revered Mentors and Grandsires",
                "interests": "Bound by state oaths to Hastinapura, yet personally wishing for Pandava vindication.",
                "risks": "Dying at the hands of the very pupils they nurtured, or surviving in a compromised state.",
                "expectations": "Expect Arjuna to honor the warrior code with courage rather than sentimental pity.",
                "icon_name": "feather"
            },
            {
                "name": "Pandava Brothers & Draupadi",
                "role": "Dispossessed Family and Comrades",
                "interests": "Vindication of justice, recovery of stolen rights, redress for Draupadi's public humiliation.",
                "risks": "Total annihilation and permanent subjugation if Arjuna refuses to lead the offensive.",
                "expectations": "Count completely on Arjuna's unrivaled archery and resolve to deliver justice.",
                "icon_name": "users"
            },
            {
                "name": "Civil Society & Future Generations",
                "role": "The Collective Polity of Aryavarta",
                "interests": "Stable governance under righteous leadership rather than tyrannical despotism.",
                "risks": "Societal collapse, breakdown of civic norms, widowhood, and anarchy if war becomes total slaughter.",
                "expectations": "That justice be upheld without burning the fabric of civilization.",
                "icon_name": "globe"
            }
        ],
        "competing_values": [
            {
                "name": "Svadharma (Role-Duty)",
                "sanskrit_term": "स्वधर्म",
                "description": "The intrinsic responsibility tied to one's station, societal mandate, and protective function.",
                "polarity": "Duty vs Compassion",
                "initial_weight": 60
            },
            {
                "name": "Karuna & Ahimsa (Compassion & Non-Harm)",
                "sanskrit_term": "करुणा / अहिंसा",
                "description": "Empathy for living beings and reluctance to inflict terminal violence on loved ones.",
                "polarity": "Compassion vs Justice",
                "initial_weight": 70
            },
            {
                "name": "Raja-Niti (Systemic Justice & Order)",
                "sanskrit_term": "राजनिति",
                "description": "Upholding legal and political accountability so tyranny does not rule unchallenged.",
                "polarity": "Accountability vs Personal Kinship",
                "initial_weight": 65
            },
            {
                "name": "Nishkama Bhava (Transcending Egocentric Attachment)",
                "sanskrit_term": "निष्काम भाव",
                "description": "Acting from objective necessity rather than personal sorrow, fear of blame, or lust for fruits.",
                "polarity": "Objectivity vs Emotional Identification",
                "initial_weight": 50
            }
        ],
        "known_information": [
            "Every peaceful diplomatic mission (including Krishna's final embassy) was haughtily rejected by Duryodhana.",
            "Bhishma and Drona, while ethically sympathetic to the Pandavas, are pledged by royal oath to fight in the Kaurava frontline.",
            "The Pandava army's morale and military capability depend overwhelmingly upon Arjuna's decisive engagement."
        ],
        "uncertain_information": [
            "The ultimate human toll of eighteen days of battle and the unintended atrocities that may unfold.",
            "Whether victory will leave any joyous peace or merely an ash-covered throne amidst widows and orphans.",
            "How deeply post-war trauma will scar the surviving rulers."
        ],
        "assumptions": [
            "Arjuna assumes that laying down his arms might save lives and shame Duryodhana into reflection.",
            "Krishna reminds him that withdrawal will not prevent the battle; it will merely ensure the slaughter of his own family by unchecked tyrants."
        ],
        "options": [
            {
                "id": "A",
                "title": "Complete Renunciation: Lay Down Arms and Retreat into Asceticism",
                "description": (
                    "Arjuna drops his bow Gandiva, declares that living on alms in the forest is superior to tasting kingdom feasts soaked in mentors' blood, "
                    "and withdraws from the battlefield unconditionally."
                ),
                "core_rationale": "Personal preservation of moral purity and complete refusal to kill mentors and relatives.",
                "advantages": [
                    "Arjuna personally does not commit the act of slaying Bhishma, Drona, or kin.",
                    "Demonstrates radical personal commitment to non-violence (Ahimsa)."
                ],
                "risks": [
                    "Leaves the Pandava army leaderless; his brothers, sons, and allies will likely be massacred.",
                    "Duryodhana's tyrannical rule is permanently entrenched without accountability.",
                    "History and peers brand Arjuna's withdrawal as moral cowardice masking as righteousness."
                ],
                "reasoning_dimensions": {
                    "responsibility": 38,
                    "strategic_thinking": 30,
                    "stakeholder_awareness": 52,
                    "long_term_thinking": 35,
                    "ethical_consistency": 60,
                    "risk_awareness": 44
                },
                "consequence": {
                    "immediate_effect": "Pandava ranks freeze in dismay. Kaurava forces cheer wildly seeing their greatest adversary collapse.",
                    "secondary_consequence": "Karna and Drona advance aggressively; without Arjuna's counter-artillery, the Pandava flank is crushed within hours.",
                    "stakeholder_impact": {
                        "Pandavas": "Disastrous defeat, execution, or permanent destitution.",
                        "Elders": "Bhishma grieves Arjuna's breakdown and the loss of chivalry.",
                        "Duryodhana": "Absolute unchecked rule over Hastinapura."
                    },
                    "strategic_impact": "Total collapse of the Pandava coalition; moral abdication masquerading as virtue.",
                    "ethical_tradeoff": "Saved personal conscience at the catastrophic expense of abandoning all dependent stakeholders.",
                    "long_term_risk": "Institutionalization of unpunished injustice across the entire subcontinent.",
                    "unintended_consequence": "His renunciation does not stop the war; others fight and die anyway, under far worse, merciless conditions."
                }
            },
            {
                "id": "B",
                "title": "Conditional Defensive Combat: Fight Only Impersonal Adversaries, Spare Elders",
                "description": (
                    "Arjuna resolves to engage in the war, but establishes strict personal rules of engagement: he will battle Duryodhana, Dushasana, "
                    "and foreign mercenaries, but deliberately avoids shooting lethal arrows at Bhishma and Drona."
                ),
                "core_rationale": "Attempting a compromise between battlefield duty and filial reverence.",
                "advantages": [
                    "Participates in defending his brothers while sparing himself the psychological guilt of slaying mentors.",
                    "Appears to balance chivalric honor with personal affection."
                ],
                "risks": [
                    "Bhishma and Drona command the Kaurava vanguard; failing to neutralize them allows them to decimate thousands of Pandava soldiers daily.",
                    "Compromised battlefield focus creates hesitation, leaving Arjuna vulnerable to lethal strikes.",
                    "Prolongs the war and multiplies overall casualties exponentially."
                ],
                "reasoning_dimensions": {
                    "responsibility": 64,
                    "strategic_thinking": 55,
                    "stakeholder_awareness": 68,
                    "long_term_thinking": 50,
                    "ethical_consistency": 58,
                    "risk_awareness": 62
                },
                "consequence": {
                    "immediate_effect": "Arjuna fights half-heartedly, countering arrows gently without pressing strategic advantages.",
                    "secondary_consequence": "Bhishma unleashes devastating divine astras that tear through the Pandava ranks on days 1–9.",
                    "stakeholder_impact": {
                        "Pandavas": "Frustration mounts; Yudhishthira questions Arjuna's dedication as their soldiers fall.",
                        "Krishna": "Forced repeatedly to intervene to prevent total slaughter.",
                        "Draupadi": "Feels betrayed that the perpetrators of injustice are treated with sentimentality."
                    },
                    "strategic_impact": "Tactical stalemate favoring the numerically superior Kaurava forces.",
                    "ethical_tradeoff": "Prioritizes personal sentimental comfort over collective survivability of his troops.",
                    "long_term_risk": "Attrition bleeding the Pandava army to the point of unconditional collapse.",
                    "unintended_consequence": "Reluctance to neutralize leaders causes vastly more rank-and-file soldiers to perish."
                }
            },
            {
                "id": "C",
                "title": "Perform Duty Without Egocentric Attachment (Nishkama Karma)",
                "description": (
                    "Recognizing that the battle is not a personal duel for vengeance or royal spoils, but a solemn systemic necessity to restore cosmic and civic order (Dharma), "
                    "Arjuna surrenders personal ego and grief, takes up Gandiva, and performs his ordained responsibility with clarity, detachment, and resolve."
                ),
                "core_rationale": "Transcending personal sorrow and desire for fruits to protect cosmic and social balance.",
                "advantages": [
                    "Restores the Pandava army's moral spine and martial parity against tyrannical usurpation.",
                    "Aligns action with systemic duty (Kshatriya dharma) rather than arbitrary emotional whim.",
                    "Sets the foundation for a lawful order where violence is constrained by principle rather than greed."
                ],
                "risks": [
                    "Unavoidable slaughter of revered teachers and kin.",
                    "Post-war psychological grief and enduring sorrow over the hollow victory.",
                    "Heavy moral responsibility for the carnage that follows."
                ],
                "reasoning_dimensions": {
                    "responsibility": 92,
                    "strategic_thinking": 88,
                    "stakeholder_awareness": 86,
                    "long_term_thinking": 84,
                    "ethical_consistency": 90,
                    "risk_awareness": 82
                },
                "consequence": {
                    "immediate_effect": "Arjuna rises with serene, unshakable focus; the sound of his conch Devadatta electrifies the allied army.",
                    "secondary_consequence": "The Pandavas maintain tactical coherence; each commander operates with disciplined clarity rather than panic.",
                    "stakeholder_impact": {
                        "Pandavas": "Secures justice, vindication, and sovereignty for righteous rule.",
                        "Society": "Deposes an unlawful, law-flouting cabal and re-establishes governance by law.",
                        "Arjuna": "Bears heavy grief, yet avoids spiritual self-delusion and cowardly abdication."
                    },
                    "strategic_impact": "Decisive strategic execution allowing victory in the face of insurmountable odds.",
                    "ethical_tradeoff": "Accepts horrific tragic cost (loss of kin) as the tragic necessity of eliminating institutional evil.",
                    "long_term_risk": "Generational grief that must be healed through compassionate governance (Shanti Parva).",
                    "unintended_consequence": "The sobering realization that even righteous war leaves deep civilizational wounds."
                }
            },
            {
                "id": "D",
                "title": "Demand an Unconditional Battlefield Summit: Halt Armies for a Final Personal Appeal",
                "description": (
                    "Arjuna steps down unarmed into the no-man's-land and calls for Bhishma, Drona, and Duryodhana to meet him in full view of both hosts, "
                    "offering his own life and exile if Duryodhana cedes even a single district to his brothers."
                ),
                "core_rationale": "A radical last-ditch gamble to prick the conscience of the elders in public view.",
                "advantages": [
                    "Exhausts every theoretical micro-possibility of human appeal before arrows fly.",
                    "Forces the Kaurava leadership to display their intransigence openly before all common soldiers."
                ],
                "risks": [
                    "High probability of treacherous assassination while vulnerable outside chariot lines.",
                    "Duryodhana has already rebuffed Krishna Himself; appealing with personal sacrifice invites contempt.",
                    "Dampens allied momentum and sows profound confusion among allied kings."
                ],
                "reasoning_dimensions": {
                    "responsibility": 60,
                    "strategic_thinking": 42,
                    "stakeholder_awareness": 72,
                    "long_term_thinking": 55,
                    "ethical_consistency": 68,
                    "risk_awareness": 48
                },
                "consequence": {
                    "immediate_effect": "A tense hush falls; warriors murmur in astonishment as Arjuna steps forward bare-chested.",
                    "secondary_consequence": "Duryodhana mocks the spectacle as pathetic theatrics born of fear of Karna and Bhishma.",
                    "stakeholder_impact": {
                        "Pandavas": "Alarmed and terrified for their champion's physical security.",
                        "Krishna": "Sternly warns Arjuna that vanity and sentimental grandstanding cannot replace disciplined duty.",
                        "Duryodhana": "Emboldened to attack the disorganized enemy."
                    },
                    "strategic_impact": "Tactical confusion that nearly forfeits the battle before it commences.",
                    "ethical_tradeoff": "Mistakes personal performative heroism for substantive ethical responsibility.",
                    "long_term_risk": "Vulnerability to surprise ambush and demoralization of allied troops.",
                    "unintended_consequence": "The elders weep in sorrow but confirm they cannot break their royal allegiance, forcing Arjuna back to his bow."
                }
            }
        ],
        "principles": [
            {
                "id": "nishkama-karma",
                "name": "Nishkama Karma (Action Free from Fruit-Attachment)",
                "sanskrit_term": "निष्काम कर्म (Bhagavad Gītā 2.47)",
                "definition": (
                    "Karmanye vadhi-karaste ma phaleshu kadachana. You have an entitlement to your action, but never to the fruits thereof. "
                    "Action must be driven by intrinsic responsibility and necessity, not egoic craving for glory or fear of personal sorrow."
                ),
                "episode_connection": (
                    "Krishna instructs Arjuna that retreating out of grief is just as egotistical as fighting out of greed. "
                    "True ethical maturity lies in discerning one's unavoidable role (Svadharma) in maintaining the world order (Lokasamgraha) and acting without paralysis."
                ),
                "modern_application": (
                    "Leaders must make painful decisions (such as restructuring, enforcing ethical policies, or whistleblowing) based on systemic duty, "
                    "rather than being immobilized by the desire to be universally liked or fear of personal popularity loss."
                ),
                "key_insight": "Detachment does not mean apathy; it means clarity free from selfish panic."
            },
            {
                "id": "svadharma-vs-paradharma",
                "name": "Svadharma vs. Paradharma (Authentic Role Duty vs. Imitated Virtue)",
                "sanskrit_term": "श्रेयान् स्वधर्मो विगुणः परधर्मात् स्वनुष्ठितात् (Gītā 3.35)",
                "definition": (
                    "Better is one's own duty, even if imperfect, than another's duty performed faultlessly. "
                    "For a protector and warrior, adopting an ascetic's withdrawal at the hour of combat is an evasion, not genuine renunciation."
                ),
                "episode_connection": (
                    "Arjuna's urge to beg for alms in the forest was not born of genuine spiritual detachment, but of emotional shock and escapism. "
                    "Abandoning one's stewardship role when others depend upon you is a breach of trust."
                ),
                "modern_application": (
                    "A project manager cannot simply act like a detached spectator when their team is facing critical failure. "
                    "Your specific organizational mandate dictates what decisions you cannot ethically abandon."
                ),
                "key_insight": "Ethics is contextual: what is virtuous for a forest hermit is dereliction of duty for a guardian."
            }
        ],
        "modern_scenario": {
            "id": "modern-arjuna-team-lead",
            "title": "The Student Lead and the Compromised Capstone",
            "domain": "Academic Leadership & Personal Loyalty",
            "context": (
                "You are the elected team lead of a 4-person senior university capstone project, whose outcome directly determines "
                "graduation honors and job offers for all members. Two days before final submission to the industry accreditation panel, "
                "you discover that your closest friend and roommate, who has struggled through severe family distress this semester, "
                "copied proprietary source code directly from a corporate GitHub repository to finish their module. If detected by the university's "
                "automated audit, the entire team risks immediate expulsion for academic fraud and loss of future accreditation."
            ),
            "dilemma": (
                "Do you report the violation immediately to save your own reputation and the team's standing, or do you protect your friend "
                "at the risk of collective ruin? How do you balance deep personal loyalty against collective accountability?"
            ),
            "parallel_to_epic": (
                "Like Arjuna, you are paralyzed because the person whose misconduct jeopardizes the collective enterprise is someone you deeply love. "
                "Fulfilling your stewardship duty feels like betrayal; shielding them imperils innocent stakeholders."
            ),
            "options": [
                {
                    "id": "A",
                    "title": "Conceal and Cover Up Privately",
                    "description": "Keep silent, rewrite the code yourself through 48 sleepless hours without informing the panel or the team, shielding your friend completely.",
                    "primary_tradeoff": "Prioritizes personal loyalty; absorbs massive exhaustion and takes extreme risk of being caught as a co-conspirator.",
                    "consequence_preview": "If any traces remain, your academic integrity is permanently shattered; your friend learns no accountability."
                },
                {
                    "id": "B",
                    "title": "Immediate Hard Escalation to Faculty Panel",
                    "description": "Report your friend directly to the examination dean without prior warning to clear the other three members from liability.",
                    "primary_tradeoff": "Total deontology; destroys the friendship and triggers your friend's immediate suspension without remediation.",
                    "consequence_preview": "The team survives academically, but you face severe peer backlash and lifelong remorse over how callously it was handled."
                },
                {
                    "id": "C",
                    "title": "Firm Accountability with Structured Remediation Window (Nishkama Approach)",
                    "description": "Confront the friend immediately with the evidence. Give them an 8-hour window to co-author an emergency clean refactor while requesting a 24-hour extension from the professor for 'module redesign', making it clear that if they refuse to replace the illicit code, you will officially inform the coordinator.",
                    "primary_tradeoff": "Balances uncompromising adherence to integrity with proactive mentorship and mutual problem-solving.",
                    "consequence_preview": "Demands intense crisis management, but protects team integrity without unnecessary cruelty, enabling your friend to take moral ownership."
                },
                {
                    "id": "D",
                    "title": "Diffuse Responsibility: Put it to an Anonymous Team Vote",
                    "description": "Present the problem to the entire team and ask them to vote anonymously on whether to report or submit as-is.",
                    "primary_tradeoff": "Abdicates leadership responsibility; turns an objective integrity crisis into a popularity contest.",
                    "consequence_preview": "Breeds toxic distrust among teammates; fails to prevent academic fraud if the vote leans towards reckless secrecy."
                }
            ]
        },
        "sources": [
            {
                "text": "The Mahābhārata: Bhīṣmaparvan",
                "parva": "Bhishma Parva",
                "chapter_section": "Bhandarkar Oriental Research Institute (BORI) Critical Edition, Vol. 7, Chapters 23–40",
                "critical_edition_ref": "BORI CE VI.23.1 – VI.40.5",
                "scholar_translation": "J.A.B. van Buitenen (University of Chicago Press, 1981) / Kisari Mohan Ganguli (1883–1896)",
                "scholarly_note": "Arjuna's collapse (vishāda) is framed not as psychological weakness, but as an existential moral crisis (Dharma-sankata) exploring the clash between deontology, virtue ethics, and consequentialism.",
                "archive_link": "https://www.gitasupersite.iitk.ac.in"
            },
            {
                "text": "Bhagavad Gītā with Commentaries",
                "parva": "Bhishma Parva",
                "chapter_section": "Chapter 2: Sāmkhya Yoga, Verses 1–11 & 47–50",
                "critical_edition_ref": "Gītā II.47 ('Karmaṇy evādhikāras te mā phaleṣu kadācana')",
                "scholar_translation": "Swami Gambhirananda (Advaita Ashrama) & S. Radhakrishnan (HarperCollins, 1948)",
                "scholarly_note": "Nishkama Karma represents an epistemological shift: detaching motivation from self-aggrandizing outcomes frees the intellect (Buddhi) for optimal moral agency under pressure.",
                "archive_link": "https://www.holy-bhagavad-gita.org"
            }
        ]
    },
    {
        "id": "krishna-peace-mission",
        "title": "Krishna's Peace Mission to Hastinapura",
        "subtitle": "Diplomacy, Exhaustion of Peaceful Means, and the Moral Foundation for Force",
        "parva": "Udyoga Parva",
        "chapter_reference": "Mahābhārata V.82–V.137 / Bhagavāna Yāna Parva",
        "characters": ["Krishna", "Duryodhana", "Dhritarashtra", "Bhishma", "Vidura"],
        "category": "Diplomacy & Conflict Prevention",
        "strategic_themes": ["Negotiation Strategy", "Conflict Escalation", "Just War Theory", "Soft Power vs Hard Power"],
        "ethical_themes": ["Sāma (Peaceful Counsel)", "Shanti (Preservation of Life)", "Moral Legitimacy", "Exhaustion of Remedies"],
        "difficulty": "Advanced",
        "estimated_time": "14-16 min",
        "order_index": 2,
        "context": (
            "After thirteen arduous years of exile, the Pandavas are legally entitled to receive their ancestral kingdom. "
            "Instead of immediately mobilizing for vengeance, Krishna undertakes a personal embassy to Hastinapura. "
            "Both Yudhishthira and Draupadi hold conflicting feelings: Yudhishthira desires peace at almost any price, "
            "while Draupadi weeps, holding her untied hair, reminding Krishna of her public humiliation. "
            "Krishna knows that Duryodhana's envy is deeply entrenched and war is virtually certain. "
            "Yet he insists on entering the tiger's den alone to deliver an uncompromising peace proposal."
        ),
        "dilemma": (
            "Why invest enormous diplomatic effort and expose oneself to humiliation and betrayal when the adversary has "
            "repeatedly proven untrustworthy? Should an ethical leader pursue diplomacy to the extreme boundary—even offering to settle "
            "for just five modest villages—or should they strike decisively when military readiness is peak?"
        ),
        "why_difficult": (
            "If Krishna offers too much compromise, it appears as weakness and demoralizes his allies; if he demands total unconditional surrender, "
            "he validates the hawk faction in Hastinapura. By exhausting every peaceful alternative in the presence of neutral kings, "
            "Krishna strips the Kauravas of moral legitimacy. But this process incurs real risks: delay, potential capture, and agonizing frustration for his supporters."
        ),
        "stakeholders": [
            {
                "name": "Krishna (The Diplomat-Statesman)",
                "role": "Ambassador for Peace & Strategic Guide",
                "interests": "Preventing the slaughter of a generation while guaranteeing justice.",
                "risks": "Hostage-taking, personal assassination attempts by Duryodhana, appearing toothless.",
                "expectations": "To serve as the voice of Dharma in the royal assembly of Hastinapura.",
                "icon_name": "compass"
            },
            {
                "name": "Duryodhana & Shakuni",
                "role": "The Intransigent Ruling Faction",
                "interests": "Total monopoly of royal power without sharing an inch of territory.",
                "risks": "Complete destruction in battle if diplomacy fails.",
                "expectations": "Expect to intimidate Krishna or lure him with lavish banquets and political flattery.",
                "icon_name": "zap"
            },
            {
                "name": "Dhritarashtra, Bhishma, & Drona",
                "role": "The Institutional Assembly of Elders",
                "interests": "Preserving the Kuru dynasty without alienating Duryodhana.",
                "risks": "Moral complicity in an avoidable genocidal war.",
                "expectations": "Desperately hope Krishna can save them from their own structural impotence.",
                "icon_name": "shield"
            },
            {
                "name": "Draupadi & The Pandava Warriors",
                "role": "Victims of Injustice Awaiting Redress",
                "interests": "Restoration of honor, dignity, and legitimate rights.",
                "risks": "Seeing their suffering bargained away for a humiliating peace of five villages.",
                "expectations": "That justice will not be compromised for hollow political optics.",
                "icon_name": "flame"
            }
        ],
        "competing_values": [
            {
                "name": "Shanti (Preservation of Human Life)",
                "sanskrit_term": "शान्ति",
                "description": "Preventing widespread carnage through diplomatic compromise and patience.",
                "polarity": "Peace vs Retribution",
                "initial_weight": 75
            },
            {
                "name": "Nyaya (Substantive Justice)",
                "sanskrit_term": "न्याय",
                "description": "Ensuring wrongdoers are held accountable and victims are fully vindicated.",
                "polarity": "Justice vs Appeasement",
                "initial_weight": 70
            },
            {
                "name": "Sāma-Upāya (Exhaustion of Diplomatic Remedies)",
                "sanskrit_term": "सामोपाय",
                "description": "The strategic principle that force is ethically legitimate only after all peaceful avenues are visibly exhausted.",
                "polarity": "Due Process vs Preemptive Strike",
                "initial_weight": 80
            }
        ],
        "known_information": [
            "Duryodhana has spent thirteen years consolidating alliances with eleven Akshauhini divisions.",
            "King Dhritarashtra is intellectually aware of justice but emotionally incapable of overruling his eldest son.",
            "Vidura and Bhishma will openly support Krishna's counsel in front of the assembled kings."
        ],
        "uncertain_information": [
            "Whether public moral shaming in open assembly can peel neutral kingdoms away from Duryodhana.",
            "Whether Duryodhana's inner circle will attempt to unlawfully imprison Krishna during the mission."
        ],
        "assumptions": [
            "War may be inevitable, but the party that demonstrably sought peace gains moral superiority in the eyes of history and neutral allies."
        ],
        "options": [
            {
                "id": "A",
                "title": "Bypass Diplomacy: Launch Immediate Surprise Offensive",
                "description": "Declare that thirteen years of bad faith are sufficient justification. Reject diplomatic emissaries and launch an immediate preemptive strike while Kaurava muster is incomplete.",
                "core_rationale": "Maximizing tactical surprise and avenging Draupadi without affording the adversary time to entrench.",
                "advantages": [
                    "Gains initial military initiative and catches Kaurava garrisons off-guard.",
                    "Satisfies the demand for swift retribution."
                ],
                "risks": [
                    "Brands the Pandavas as warmongering aggressors across Aryavarta.",
                    "Neutral kings align with Hastinapura out of sympathy for an unprovoked attack.",
                    "Destroys any moral claim to be the defenders of Dharma."
                ],
                "reasoning_dimensions": {
                    "responsibility": 45,
                    "strategic_thinking": 50,
                    "stakeholder_awareness": 40,
                    "long_term_thinking": 35,
                    "ethical_consistency": 40,
                    "risk_awareness": 50
                },
                "consequence": {
                    "immediate_effect": "Pandava armies march aggressively; surprise victories in border territories.",
                    "secondary_consequence": "Outraged public sentiment across India; kings rally to defend the sovereign throne of Hastinapura.",
                    "stakeholder_impact": {
                        "Allied Kings": "Deep discomfort with being dragged into unprovoked war.",
                        "Duryodhana": "Portrays himself as the noble defender against lawless rebels.",
                        "Pandavas": "Lose high moral ground and international legitimacy."
                    },
                    "strategic_impact": "Tactical advance negated by devastating diplomatic isolation.",
                    "ethical_tradeoff": "Sacrifices legitimate process for violent expediency.",
                    "long_term_risk": "Generational condemnation as aggressors who destroyed peace.",
                    "unintended_consequence": "Neutral powers mobilize against them, turning the war unwinnable."
                }
            },
            {
                "id": "B",
                "title": "Unconditional Conciliation: Accept Whatever Crumbs Are Granted",
                "description": "Send a meek petition begging Dhritarashtra to grant any small pension or village, promising that the Pandavas will never raise arms under any circumstances.",
                "core_rationale": "Absolute preservation of physical life and complete avoidance of war at all costs.",
                "advantages": [
                    "Zero battlefield deaths in the short term.",
                    "Avoids family bloodshed completely."
                ],
                "risks": [
                    "Legitimizes usurpation, robbery, and the public disrobing of women as acceptable royal practice.",
                    "Pandavas remain powerless vassals subject to eventual assassination by Duryodhana.",
                    "Destroys societal rule of law."
                ],
                "reasoning_dimensions": {
                    "responsibility": 30,
                    "strategic_thinking": 25,
                    "stakeholder_awareness": 45,
                    "long_term_thinking": 20,
                    "ethical_consistency": 35,
                    "risk_awareness": 30
                },
                "consequence": {
                    "immediate_effect": "Duryodhana laughs contemptuously in court and casts the Pandavas aside.",
                    "secondary_consequence": "The Kaurava regime intensifies tyranny, knowing no force exists to check them.",
                    "stakeholder_impact": {
                        "Draupadi": "Total destruction of dignity and betrayal by her protectors.",
                        "Pandavas": "Living as humiliated second-class dependents.",
                        "Common Citizens": "Subjected to whimsical authoritarian governance."
                    },
                    "strategic_impact": "Total capitulation disguised as pious humility.",
                    "ethical_tradeoff": "Abandons justice and victim redress for cowardly survival.",
                    "long_term_risk": "Institutionalization of violence and extortion as state policy.",
                    "unintended_consequence": "Duryodhana eventually poisons or ambushes them anyway once their allies disband."
                }
            },
            {
                "id": "C",
                "title": "Principled Embassy with Extreme Compromise (The Five Villages Offer)",
                "description": (
                    "Travel personally to Hastinapura in dignified royal state. Reject Duryodhana's seductive banquets to stay at Vidura's modest home. "
                    "In open court, make an eloquent appeal for peace, reducing the Pandava demand from half the kingdom to merely five villages: "
                    "Indraprastha, Vrikasthala, Jayanta, Varanavata, and one other. If rejected, reveal the catastrophic consequences of war openly."
                ),
                "core_rationale": "Exhausting all peaceful means while visibly putting the entire burden of war upon Duryodhana's intransigence.",
                "advantages": [
                    "Demonstrates unassailable moral reasonableness before the entire council of elders.",
                    "If Duryodhana refuses five villages, his greed is unmasked beyond any defense, winning the moral consensus of the world.",
                    "Validates subsequent military action as an inescapable duty of last resort."
                ],
                "risks": [
                    "Duryodhana may attempt treacherous arrest of the envoy.",
                    "Draupadi and Bhima feel deep temporary anguish that five villages were offered.",
                    "War remains likely, but the burden of starting it is placed squarely on the enemy."
                ],
                "reasoning_dimensions": {
                    "responsibility": 95,
                    "strategic_thinking": 96,
                    "stakeholder_awareness": 92,
                    "long_term_thinking": 94,
                    "ethical_consistency": 90,
                    "risk_awareness": 88
                },
                "consequence": {
                    "immediate_effect": "The elders (Bhishma, Drona, Vidura) weep in court and praise Krishna's extraordinary magnanimity.",
                    "secondary_consequence": "Duryodhana arrogantly declares: 'I will not yield even as much earth as can be pierced by the point of a needle!'",
                    "stakeholder_impact": {
                        "Neutral Kings": "Decide to align with the Pandavas or stay neutral, seeing Duryodhana as an irrational warmonger.",
                        "Pandavas": "United with clear conscience; every soldier knows they fight an unprovoked tyrant.",
                        "Krishna": "Demonstrates the universal ethical standard for just war."
                    },
                    "strategic_impact": "Achieves absolute moral and diplomatic legitimacy, fracturing Kaurava internal morale.",
                    "ethical_tradeoff": "Accepts temporary tension with aggrieved allies in order to secure permanent ethical justification.",
                    "long_term_risk": "War cannot be prevented, but its moral foundation is rock-solid.",
                    "unintended_consequence": "Duryodhana attempts to arrest Krishna, revealing his absolute contempt for diplomatic immunity."
                }
            },
            {
                "id": "D",
                "title": "Subversive Alliance Fracturing: Secretly Offer the Crown to Karna",
                "description": "Engage in bilateral backroom diplomacy: reveal Karna's true birth as Kunti's firstborn and offer him the supreme emperorship of the Pandava empire if he abandons Duryodhana.",
                "core_rationale": "Decapitating Duryodhana's martial confidence by stripping away his chief champion without fighting.",
                "advantages": [
                    "If successful, prevents the war overnight by collapsing Kaurava military capability.",
                    "Offers Karna the royal honors and recognition denied to him his entire life."
                ],
                "risks": [
                    "Karna's code of loyalty to Duryodhana is deep; rejection may cement his resolve.",
                    "Bypasses Yudhishthira's legal right to the throne without his consent.",
                    "Carries the scent of manipulative realpolitik."
                ],
                "reasoning_dimensions": {
                    "responsibility": 72,
                    "strategic_thinking": 88,
                    "stakeholder_awareness": 78,
                    "long_term_thinking": 70,
                    "ethical_consistency": 62,
                    "risk_awareness": 75
                },
                "consequence": {
                    "immediate_effect": "Karna is deeply moved and sheds tears at discovering his mother, yet refuses to betray the friend who stood by him.",
                    "secondary_consequence": "While Karna stays with Duryodhana, his internal psychological certainty is permanently fractured.",
                    "stakeholder_impact": {
                        "Karna": "Promises Krishna he will not slay any Pandava except Arjuna.",
                        "Duryodhana": "Unaware that his chief warrior has made a secret psychological concession.",
                        "Pandavas": "Their four younger brothers are secretly guaranteed survival by Karna's vow."
                    },
                    "strategic_impact": "Masterful psychological neutralization that saves four lives, though the war proceeds.",
                    "ethical_tradeoff": "Employs high-stakes secrecy and emotional revelation for strategic containment.",
                    "long_term_risk": "Karna enters the battle with a divided heart.",
                    "unintended_consequence": "Elevates Karna's moral stature while securing the ultimate survival of the Pandava line."
                }
            }
        ],
        "principles": [
            {
                "id": "sama-dana-bheda-danda",
                "name": "The Four Upāyas of Rajanīti (Hierarchy of Statecraft)",
                "sanskrit_term": "साम, दान, भेद, दण्ड",
                "definition": (
                    "Classical Indian governance insists on four sequential methods: Sāma (conciliation and discourse), "
                    "Dāna (concession, compensation, gifting), Bheda (division, exposing contradictions), and Danda (use of lawful force). "
                    "Force (Danda) is legitimate only when Sāma, Dāna, and Bheda have been honestly exhausted."
                ),
                "episode_connection": (
                    "Krishna's embassy embodies the rigorous adherence to Sāma and Dāna (offering to take five villages). "
                    "Only when Duryodhana threatens the ambassador himself does Danda become the inevitable, sanctioned duty."
                ),
                "modern_application": (
                    "In corporate conflicts, labor disputes, or international diplomacy, legal litigation or coercive termination "
                    "must be preceded by demonstrable, transparent efforts at conciliation and fair mediation."
                ),
                "key_insight": "A just outcome requires not only a just cause, but a just and exhaustive process."
            }
        ],
        "modern_scenario": {
            "id": "modern-krishna-mediation",
            "title": "The Divided Committee and the Threat to Walk Out",
            "domain": "Team Leadership & Conflict Mediation",
            "context": (
                "You are an elected student council coordinator asked to mediate a bitter dispute between two founding heads "
                "of an annual campus festival. After a heated argument over creative direction, one organizer takes an all-or-nothing stance: "
                "either the other organizer is removed from the committee completely, or they will pull their volunteer crew and cancel "
                "the festival's primary venue booking. The event is scheduled in two weeks, and hundreds of students have prepared for months."
            ),
            "dilemma": (
                "Do you capitulate to the ultimatum to save the event, take a side and expel one leader, or present a firm, "
                "uncompromising compromise that protects shared responsibility—even if the stubborn party threatens to walk away?"
            ),
            "parallel_to_epic": (
                "Like Krishna entering Hastinapura, you face an intransigent party demanding total submission. "
                "You must decide whether to appease them for temporary peace or exhaust every fair diplomatic remedy to preserve institutional integrity."
            ),
            "options": [
                {
                    "id": "A",
                    "title": "Capitulate to the Ultimatum and Remove the Rival",
                    "description": "Give in to the demand and quietly remove the other organizer to ensure the festival takes place.",
                    "primary_tradeoff": "Guarantees the event runs on schedule, but rewards bullying and sets a toxic precedent of appeasement.",
                    "consequence_preview": "The festival happens, but mutual trust collapses and future leaders learn that threats win arguments."
                },
                {
                    "id": "B",
                    "title": "Expel the Demanding Organizer Immediately",
                    "description": "Reject the ultimatum on the spot and expel the demanding leader for threatening the festival.",
                    "primary_tradeoff": "Upholds principles firmly, but immediately loses the venue booking and risks canceling the entire event.",
                    "consequence_preview": "Causes immediate chaos and volunteer walkouts before alternative plans can be made."
                },
                {
                    "id": "C",
                    "title": "The Measured Compromise (The 'Five Villages' Approach)",
                    "description": "Convene both organizers before the broader council. Propose a clear division of responsibilities with neutral oversight. Make it clear that both are expected to serve the community, but if one refuses a fair division, the council will proceed without them.",
                    "primary_tradeoff": "Demands patience and risks a walkout, but establishes clear, fair terms that put the burden of bad faith on the unreasonable party.",
                    "consequence_preview": "If accepted, the festival succeeds collaboratively; if rejected, the council rallies behind you with a clean conscience to find an alternative venue."
                },
                {
                    "id": "D",
                    "title": "Step Down and Refuse to Mediate",
                    "description": "Tell both parties that since they cannot agree as adults, they should solve it themselves without you.",
                    "primary_tradeoff": "Protects you from blame, but abandons the community when leadership is most needed.",
                    "consequence_preview": "The festival dissolves into public acrimony."
                }
            ]
        },
        "sources": [
            {
                "text": "The Mahābhārata: Udyogaparvan",
                "parva": "Udyoga Parva",
                "chapter_section": "BORI Critical Edition, Vol. 6, Bhagavāna Yāna Parva, Chapters 82–137",
                "critical_edition_ref": "BORI CE V.82.1 – V.137.25",
                "scholar_translation": "J.A.B. van Buitenen (University of Chicago Press, 1978) / K.M. Ganguli",
                "scholarly_note": "Krishna's discourse in Dhritarashtra's court is regarded as the pinnacle of ancient Indian diplomatic realism and normative just war ethics.",
                "archive_link": "https://www.sacred-texts.com/hin/m05/index.htm"
            }
        ]
    },
    {
        "id": "yudhishthira-yaksha",
        "title": "Yudhishthira and the Yaksha at the Enchanted Pool",
        "subtitle": "Patience, Restraint, and Prioritisation under Existential Crisis",
        "parva": "Vana Parva",
        "chapter_reference": "Mahābhārata III.295–III.299 / Araneya Parva (Yaksha Prashna)",
        "characters": ["Yudhishthira", "Yaksha (Dharma)", "Nakula", "Sahadeva", "Arjuna", "Bhima"],
        "category": "Ethical Restraint & Prioritisation",
        "strategic_themes": ["Decision-Making Under Duress", "Impulse Control", "Epistemic Humility", "Equity vs Equality"],
        "ethical_themes": ["Dharma (Cosmic Justice)", "Anrishamsya (Compassionate Non-Cruelty)", "Patience (Dhriti)", "Reverence for Knowledge"],
        "difficulty": "Intermediate",
        "estimated_time": "12-14 min",
        "order_index": 3,
        "context": (
            "During the final phase of their twelve-year forest exile, the Pandava brothers are exhausted, dehydrated, and pursuing a deer "
            "that entangled a poor Brahmana's fire-churning sticks in its antlers. Nakula is sent to find water. "
            "He discovers a pristine crystal lake, but as he bends to drink, an unseen crane/voice warns: "
            "'Do not drink without first answering my questions; this pool belongs to me.' "
            "Tormented by parching thirst, Nakula disregards the warning, drinks, and collapses dead. "
            "One by one, Sahadeva, Arjuna, and mighty Bhima arrive, dismiss the invisible voice with martial arrogance, drink, and drop dead. "
            "Finally, King Yudhishthira arrives. Seeing his four invincible brothers lying dead on the bank like uprooted trees, "
            "his heart shatters with grief. Yet when the voice warns him, Yudhishthira lowers his hands, controls his burning thirst, and bows."
        ),
        "dilemma": (
            "When faced with mortal panic, biological agony, and the apparent slaughter of one's entire family, does one lash out violently, "
            "succumb to immediate impulse, or subordinate pride to engage in patient intellectual dialogue? "
            "And when granted the resurrection of only ONE brother, whom should he choose?"
        ),
        "why_difficult": (
            "The first test is emotional regulation: conquering desperate biological thirst through self-mastery. "
            "The second test is supreme ethical prioritisation: given the chance to revive ONE brother, strategic logic screams for Bhima (physical muscle) "
            "or Arjuna (unrivaled archer) so Yudhishthira can win the coming war against Hastinapura. "
            "Choosing Nakula (his stepmother Madri's son) appears strategically suicidal, yet represents the highest virtue: Anrishamsya (non-cruelty and equal filial justice)."
        ),
        "stakeholders": [
            {
                "name": "Yudhishthira",
                "role": "The Righteous King & Oldest Pandava",
                "interests": "Reviving his brothers, quenching deadly thirst, keeping faith with virtue.",
                "risks": "Instant death from poisoning or divine curse; losing his brothers forever.",
                "expectations": "To govern his conduct by cosmic truth even in the abyss of despair.",
                "icon_name": "shield"
            },
            {
                "name": "The Yaksha (Lord Dharma)",
                "role": "Cosmic Examiner & Guardian of the Pool",
                "interests": "Testing whether Yudhishthira's famed righteousness is genuine or mere royal veneer.",
                "risks": "None; possesses absolute metaphysical power over the pool.",
                "expectations": "Direct, profound answers reflecting self-restraint and wisdom.",
                "icon_name": "sun"
            },
            {
                "name": "Kunti & Madri (The Two Mothers)",
                "role": "The Ancestral Matriarchs",
                "interests": "Equal preservation of both maternal lineages in the royal succession.",
                "risks": "If only Kunti's sons survive, Madri is left entirely childless in eternity.",
                "expectations": "That their son would treat both mothers with impartial fairness.",
                "icon_name": "heart"
            }
        ],
        "competing_values": [
            {
                "name": "Anrishamsya (Non-Cruelty and Impartial Equity)",
                "sanskrit_term": "आनृशंस्य",
                "description": "Active absence of spite, greed, and partiality; treating step-kin with equal devotion as full blood.",
                "polarity": "Impartial Justice vs Strategic Expediency",
                "initial_weight": 85
            },
            {
                "name": "Strategic Utility (Military Preparedness for War)",
                "sanskrit_term": "बल-नीति",
                "description": "Securing military champions (Arjuna or Bhima) essential for defeating the Kauravas.",
                "polarity": "Pragmatic Survival vs Idealist Virtue",
                "initial_weight": 65
            },
            {
                "name": "Dhriti & Dama (Patience and Sense-Restraint)",
                "sanskrit_term": "धृति / दम",
                "description": "The capacity to pause biological impulses and emotional frenzy in crisis.",
                "polarity": "Restraint vs Impulsive Action",
                "initial_weight": 90
            }
        ],
        "known_information": [
            "Four peerless warriors who could defeat gods lie completely dead without physical weapon wounds.",
            "The unseen presence has demonstrated real lethal power.",
            "The voice explicitly promises: answer my questions, and you may live and drink."
        ],
        "uncertain_information": [
            "Whether the dead brothers can actually be brought back to life or if the voice is taunting.",
            "The true celestial identity of the Yaksha."
        ],
        "assumptions": [
            "Martial force cannot conquer an unseen spiritual rule of the domain."
        ],
        "options": [
            {
                "id": "A",
                "title": "Violent Retaliation: Loose Divine Astras into the Forest and Drink",
                "description": "Assume the voice is an illusion created by a forest demon. Fire arrows in all ten directions, cast spells, and drink from the water to quench thirst.",
                "core_rationale": "Asserting warrior pride and refusing to submit to an invisible interrogator.",
                "advantages": ["Maintains martial defiance; refuses to kowtow."],
                "risks": ["Immediate death, following the identical fate of Arjuna and Bhima.", "Total extinction of the Pandava line."],
                "reasoning_dimensions": {
                    "responsibility": 20,
                    "strategic_thinking": 15,
                    "stakeholder_awareness": 25,
                    "long_term_thinking": 10,
                    "ethical_consistency": 20,
                    "risk_awareness": 18
                },
                "consequence": {
                    "immediate_effect": "Yudhishthira drinks defiantly and collapses dead beside his brothers.",
                    "secondary_consequence": "The Pandava lineage is erased in the forest; Duryodhana rules uncontested forever.",
                    "stakeholder_impact": {
                        "Pandavas": "Complete annihilation through arrogant obstinacy.",
                        "Kunti": "Left childless in Hastinapura."
                    },
                    "strategic_impact": "Catastrophic failure driven by ego and impulse.",
                    "ethical_tradeoff": "Pride chosen over wisdom.",
                    "long_term_risk": "Extinction of the family.",
                    "unintended_consequence": "The simplest lesson in restraint is failed."
                }
            },
            {
                "id": "B",
                "title": "Answer Patiently, Then Strategically Request Arjuna or Bhima's Revival",
                "description": "Answer the Yaksha's philosophical queries with brilliant scholarship. When granted one life, choose Arjuna or Bhima so the team has military power to conquer Hastinapura.",
                "core_rationale": "Pragmatic balance: show intellectual respect, but prioritize military survival when given an asset choice.",
                "advantages": [
                    "Guarantees that the Pandavas have an invincible military champion for the coming war.",
                    "Understood by conventional political realism as the only sensible choice."
                ],
                "risks": [
                    "Leaves Madri's lineage totally extinct, violating the sacred vow of equal maternal honor.",
                    "Reveals that Yudhishthira prioritizes power over supreme impartial justice."
                ],
                "reasoning_dimensions": {
                    "responsibility": 70,
                    "strategic_thinking": 78,
                    "stakeholder_awareness": 65,
                    "long_term_thinking": 72,
                    "ethical_consistency": 60,
                    "risk_awareness": 74
                },
                "consequence": {
                    "immediate_effect": "The Yaksha revives Arjuna or Bhima as requested.",
                    "secondary_consequence": "Yudhishthira survives with a warrior brother, but carries lifelong guilt that he condemned Nakula and Sahadeva to death.",
                    "stakeholder_impact": {
                        "Madri's Line": "Extinguished forever.",
                        "Kunti": "Carries the grief of her sister-wife's total loss.",
                        "Yaksha": "Acknowledges intellectual competence, but finds spiritual partiality."
                    },
                    "strategic_impact": "Recovers military capability, but fails the ultimate test of pure Dharma.",
                    "ethical_tradeoff": "Sacrifices equal justice across family branches for military pragmatism.",
                    "long_term_risk": "Deep internal moral compromise.",
                    "unintended_consequence": "The Yaksha does not revive the remaining brothers, leaving them permanently hobbled."
                }
            },
            {
                "id": "C",
                "title": "Restraint & Supreme Impartiality: Answer with Wisdom and Request Nakula (Anrishamsya)",
                "description": (
                    "Control thirst with iron will. Answer the Yaksha's 120 questions on grief, time, truth, and society with luminous clarity. "
                    "When offered the revival of only ONE brother, ask for Nakula, explaining: 'My father had two wives, Kunti and Madri. "
                    "I, a son of Kunti, am alive; it is only just that a son of Madri also lives so that neither mother is bereft.'"
                ),
                "core_rationale": "Anrishamsya (transcending self-interest to uphold equal love and justice for both maternal lines).",
                "advantages": [
                    "Demonstrates total liberation from narrow partisan favoritism.",
                    "Elevates ethical principle above pragmatic self-preservation.",
                    "Proves to the celestial examiner that Dharma is alive in deed, not merely word."
                ],
                "risks": [
                    "If the Yaksha revives only one, Yudhishthira enters the war without his greatest archer (Arjuna) or strongest champion (Bhima)."
                ],
                "reasoning_dimensions": {
                    "responsibility": 98,
                    "strategic_thinking": 90,
                    "stakeholder_awareness": 96,
                    "long_term_thinking": 95,
                    "ethical_consistency": 98,
                    "risk_awareness": 92
                },
                "consequence": {
                    "immediate_effect": "The Yaksha is overwhelmed with joy and reverence: 'O King, since you cherish Anrishamsya above profit and power, ALL your brothers shall rise!'",
                    "secondary_consequence": "All four brothers awaken refreshed, their thirst quenched, healed and stronger than before.",
                    "stakeholder_impact": {
                        "All Brothers": "Restored to life with deep reverence for Yudhishthira's transcendent leadership.",
                        "Lord Dharma": "Reveals His celestial identity and grants them boons of remaining undetected in their 13th year.",
                        "Civilization": "Receives the eternal philosophical treasure of the Yaksha Prashna."
                    },
                    "strategic_impact": "By placing ultimate justice above narrow pragmatism, gains 100% of his assets back plus divine boons.",
                    "ethical_tradeoff": "Risked conventional utility for absolute moral consistency—and unlocked the highest possible outcome.",
                    "long_term_risk": "None; established unbreakable moral authority as Dharmaraja.",
                    "unintended_consequence": "The test transforms from a death trap into the greatest blessing of their exile."
                }
            },
            {
                "id": "D",
                "title": "Offer Self-Sacrifice in Place of All Four Brothers",
                "description": "Refuse to drink and refuse to pick among brothers. Ask the Yaksha to take Yudhishthira's life in exchange for reviving all four brothers together.",
                "core_rationale": "Martyrdom and noble self-abnegation.",
                "advantages": ["Emotionally moving display of fraternal sacrifice."],
                "risks": [
                    "Evades the ethical judgment asked of a King.",
                    "Leaves the four surviving brothers leaderless and directionless.",
                    "Breaches the royal duty to lead the people."
                ],
                "reasoning_dimensions": {
                    "responsibility": 55,
                    "strategic_thinking": 40,
                    "stakeholder_awareness": 65,
                    "long_term_thinking": 35,
                    "ethical_consistency": 60,
                    "risk_awareness": 45
                },
                "consequence": {
                    "immediate_effect": "The Yaksha chuckles and rejects the emotional evasion: 'A King must discern and decide, not escape through death.'",
                    "secondary_consequence": "Forces Yudhishthira back to the substantive questions.",
                    "stakeholder_impact": {
                        "Yaksha": "Demands cognitive reasoning rather than theatrical emotional sacrifice."
                    },
                    "strategic_impact": "Delays the test without solving the fundamental problem.",
                    "ethical_tradeoff": "Substitutes sentimental martyrdom for mature ethical discernment.",
                    "long_term_risk": "Vulnerability to impulsive despair.",
                    "unintended_consequence": "Reminded that true Dharma requires living and making difficult choices, not running to the grave."
                }
            }
        ],
        "principles": [
            {
                "id": "anrishamsya-paramo-dharmah",
                "name": "Anrishamsya (Non-Cruelty / Compassionate Equity as Supreme Dharma)",
                "sanskrit_term": "आनृशंस्यं परो धर्मः (Mahābhārata III.297.71)",
                "definition": (
                    "Yudhishthira explicitly states in the text: 'Anrishamsyam paro dharmah'—Non-cruelty, fairness, and the deliberate refusal "
                    "to inflict harm or partiality, even upon step-relations, is the highest virtue of human existence."
                ),
                "episode_connection": (
                    "By selecting Nakula rather than his own uterine brothers Bhima or Arjuna, Yudhishthira demonstrated that justice "
                    "cannot be bent to benefit one's inner clan. His commitment to maternal equity was absolute."
                ),
                "modern_application": (
                    "In resource allocation, organizational triage, or inheritance, leaders must not privilege their 'in-group' "
                    "or star performers while starving other foundational stakeholders."
                ),
                "key_insight": "Fairness shines brightest when choosing it costs you your most valuable pragmatic advantage."
            }
        ],
        "modern_scenario": {
            "id": "modern-yaksha-clinic-medicine",
            "title": "The Flooded Clinic and the Single Dose",
            "domain": "Fairness, Kinship & Impartial Triage",
            "context": (
                "During a severe monsoon storm, road access to your town is flooded, cutting off the small clinic where you are volunteering. "
                "There is only one remaining refrigerated dose of specialized respiratory medicine left in stock. Two patients arrive at the same time: "
                "your own teenage cousin with a serious asthma attack, and an elderly laborer from across the river with an advanced, life-threatening attack. "
                "The doctor is away, and you must decide who receives the single dose while emergency services are delayed."
            ),
            "dilemma": (
                "Do you give the medicine to your own family member, or allocate it strictly based on clinical severity to an unknown stranger?"
            ),
            "parallel_to_epic": (
                "Like Yudhishthira choosing Madri's son Nakula to maintain equal honor and justice between two families rather than favoring his full brother, "
                "you face the fundamental test of whether compassion and fairness (Ānṛśaṁsya) extend beyond your immediate bloodline."
            ),
            "options": [
                {
                    "id": "A",
                    "title": "Treat Your Family Member First",
                    "description": "Administer the medicine to your cousin to ensure your family's safety.",
                    "primary_tradeoff": "Protects your family bond, but deprives a patient in more critical medical distress of survival care.",
                    "consequence_preview": "Your cousin recovers, but the elderly patient suffers permanent damage or death, leaving you with heavy moral remorse."
                },
                {
                    "id": "B",
                    "title": "Strict Impartial Care Based on Medical Need",
                    "description": "Administer the dose to the laborer whose condition is immediately life-threatening, while continuously monitoring and comforting your cousin with secondary support.",
                    "primary_tradeoff": "Endures personal agony over your cousin's distress, but upholds the highest standard of universal fairness and duty.",
                    "consequence_preview": "Saves the life in greatest peril; earns deep respect for true moral impartiality under crisis."
                },
                {
                    "id": "C",
                    "title": "Split the Dose Equally Between Both",
                    "description": "Divide the single dose into two half-doses to avoid choosing.",
                    "primary_tradeoff": "An emotional compromise that risks under-dosing both patients, rendering the treatment ineffective for both.",
                    "consequence_preview": "Neither patient receives a therapeutic threshold; both remain at severe medical risk."
                },
                {
                    "id": "D",
                    "title": "Delay the Decision Waiting for the Doctor",
                    "description": "Wait by the door hoping a medical professional arrives in time.",
                    "primary_tradeoff": "Abdicates the decision out of fear of responsibility.",
                    "consequence_preview": "Wastes critical minutes while both patients worsen."
                }
            ]
        },
        "sources": [
            {
                "text": "The Mahābhārata: Āraṇyakaparvan",
                "parva": "Vana Parva",
                "chapter_section": "BORI Critical Edition, Vol. 4, Chapters 295–299 (Yaksha-Praśna)",
                "critical_edition_ref": "BORI CE III.297.71 ('ānṛśaṁsyaṁ paro dharmaḥ')",
                "scholar_translation": "J.A.B. van Buitenen (Univ. of Chicago Press, 1975) / V.S. Sukthankar",
                "scholarly_note": "The dialogue highlights epistemic humility: wisdom begins when the human actor recognizes that life's resources are conditional gifts governed by cosmic order (Dharma).",
                "archive_link": "https://www.sacred-texts.com/hin/m03/index.htm"
            }
        ]
    },
    {
        "id": "vidura-counsel",
        "title": "Vidura's Midnight Counsel to the Sleepless King",
        "subtitle": "Speaking Truth to Blind Power and the Courage of Ethical Dissent",
        "parva": "Udyoga Parva",
        "chapter_reference": "Mahābhārata V.33–V.40 / Prajāgara Parva (Vidura Nīti)",
        "characters": ["Vidura", "King Dhritarashtra", "Sanjaya"],
        "category": "Governance & Truth to Power",
        "strategic_themes": ["Advisory Ethics", "Cognitive Dissonance", "Confirmation Bias", "Risk Warning Systems"],
        "ethical_themes": ["Satya (Truthful Speech)", "Raja-Dharma (Governance Ethics)", "Aparigraha (Freedom from Corrupt Motive)", "Courage of Conscience"],
        "difficulty": "Intermediate",
        "estimated_time": "12-14 min",
        "order_index": 4,
        "context": (
            "Sanjaya has returned from the Pandava camp bearing an unyielding message from Yudhishthira: justice or total war. "
            "King Dhritarashtra, paralyzed with anxiety and burning with insomnia, summons his prime minister and half-brother Vidura in the middle of the night. "
            "Dhritarashtra is desperate for soothing comfort, wanting Vidura to validate his choices and ease his gnawing fear. "
            "Vidura is of low birth (born of a maid-servant) and serves at the King's pleasure. He knows that speaking the unvarnished truth "
            "will infuriate Duryodhana, alienate the royal court, and bring him personal political peril."
        ),
        "dilemma": (
            "When advising a powerful, emotionally compromised sovereign who desires validation rather than truth, "
            "does the counselor provide diplomatic palliative flattery to preserve their position and influence, "
            "or do they deliver relentless, uncomfortable ethical truth knowing it may be ignored or punished?"
        ),
        "why_difficult": (
            "If Vidura speaks pleasant falsehoods (Priyam Nanritam), he maintains his royal standing and can perhaps soften harsh decrees later, "
            "but he becomes complicit in the destruction of the kingdom. If he speaks brutal truth (A-priya Satya), he risks exile, "
            "and Dhritarashtra may close his ears completely. Vidura Nīti investigates the exact duty of an advisor in an echo chamber of hubris."
        ),
        "stakeholders": [
            {
                "name": "Vidura (The Sage Counselor)",
                "role": "Prime Minister & Conscience of Hastinapura",
                "interests": "Upholding cosmic truth, preventing state suicide, maintaining ethical purity.",
                "risks": "Exile, dismissal, execution, or total irrelevance.",
                "expectations": "To serve as the incorruptible mirror of truth for the blind king.",
                "icon_name": "feather"
            },
            {
                "name": "Dhritarashtra (The King)",
                "role": "Sovereign Blinded by Paternal Attachment",
                "interests": "Easing nocturnal panic, securing his son's reign, hearing soothing reassurance.",
                "risks": "Total destruction of his dynasty, eternal civilizational disgrace.",
                "expectations": "Wants to be comforted without being asked to discipline his son.",
                "icon_name": "eye-off"
            },
            {
                "name": "The Citizens of Hastinapura",
                "role": "The Voiceless Populace",
                "interests": "Living in peace under a lawful administration without being conscripted into an avoidable war.",
                "risks": "Devastation, taxes, famine, loss of husbands and sons.",
                "expectations": "That wise ministers in the palace will protect them from reckless princes.",
                "icon_name": "users"
            }
        ],
        "competing_values": [
            {
                "name": "Satya (Fearless Unvarnished Truth)",
                "sanskrit_term": "सत्य",
                "description": "Speaking the factual and moral reality without flattery or dilution.",
                "polarity": "Brutal Truth vs Diplomatic Comfort",
                "initial_weight": 90
            },
            {
                "name": "Kalyana (Compassion for the Deluded Sovereign)",
                "sanskrit_term": "कल्याण",
                "description": "Attempting to guide the fragile king gently so he does not defensively shut down.",
                "polarity": "Gentle Persuasion vs Direct Condemnation",
                "initial_weight": 65
            },
            {
                "name": "Atma-Raksha (Advisor Self-Preservation to Retain Influence)",
                "sanskrit_term": "आत्मरक्षा",
                "description": "Surviving politically so one is still present to moderate the next crisis.",
                "polarity": "Long-Term Presence vs One-Time Confrontation",
                "initial_weight": 40
            }
        ],
        "known_information": [
            "Dhritarashtra acknowledges in private that Duryodhana is reckless and evil, yet says: 'My heart follows my son.'",
            "Vidura has no military army of his own; his sole authority is intellectual and moral authority.",
            "The assembly of Hastinapura is paralyzed by fear of Duryodhana and Karna."
        ],
        "uncertain_information": [
            "Whether deep moral diagnosis can awaken Dhritarashtra's dormant sense of shame.",
            "How soon Duryodhana will retaliate if he discovers Vidura's frank counsel."
        ],
        "assumptions": [
            "An advisor who stays silent during corruption becomes an accomplice to its consequences."
        ],
        "options": [
            {
                "id": "A",
                "title": "Diplomatic Palliative Comfort: Soothe the King's Anxiety",
                "description": "Tell Dhritarashtra what he wants to hear: praise the strength of his armies, promise that fate will protect Hastinapura, and advise gentle patience.",
                "core_rationale": "Preserving access to power and maintaining peace in the royal chamber.",
                "advantages": ["Protects Vidura's ministerial seat and avoids the king's anger."],
                "risks": [
                    "Allows the king to drift back into complacency.",
                    "Deprives the state of its last moral brake before the cliff.",
                    "Vidura becomes morally complicit in the war."
                ],
                "reasoning_dimensions": {
                    "responsibility": 25,
                    "strategic_thinking": 30,
                    "stakeholder_awareness": 40,
                    "long_term_thinking": 20,
                    "ethical_consistency": 25,
                    "risk_awareness": 35
                },
                "consequence": {
                    "immediate_effect": "Dhritarashtra sleeps peacefully that night, comforted by empty words.",
                    "secondary_consequence": "No corrective action is taken; Duryodhana finalizes war mobilization unchecked.",
                    "stakeholder_impact": {
                        "Kingdom": "Hurtles irrevocably toward civil war.",
                        "Vidura": "Becomes a hollow courtier whose wisdom is neutralized."
                    },
                    "strategic_impact": "Loss of the final intervention opportunity to prevent war.",
                    "ethical_tradeoff": "Sold truth for personal security and temporary tranquility.",
                    "long_term_risk": "Total state collapse.",
                    "unintended_consequence": "The king later blames Vidura for not shouting loudly when danger was clear."
                }
            },
            {
                "id": "B",
                "title": "Unsparing Diagnostic Truth (The Path of Vidura Nīti)",
                "description": (
                    "Deliver a masterclass in governance ethics: dissect the eight causes of ruin, expose the king's fatal blind spot (Moha for his son), "
                    "and explicitly tell him: 'Renounce Duryodhana to save your family; sacrifice one individual for a village, and a village for the kingdom. "
                    "A true friend speaks the bitter medicine, not honeyed poison.'"
                ),
                "core_rationale": "Fulfilling the sacred obligation of an advisor to speak total truth without fear or favor.",
                "advantages": [
                    "Maintains absolute moral integrity and clarity of statecraft.",
                    "Creates an enduring constitutional document of ethical governance for humanity.",
                    "Forces the sovereign to confront his own psychological complicity."
                ],
                "risks": [
                    "Dhritarashtra may weep in helplessness and reject the counsel anyway.",
                    "Duryodhana subsequently insults and threatens Vidura in public assembly."
                ],
                "reasoning_dimensions": {
                    "responsibility": 96,
                    "strategic_thinking": 88,
                    "stakeholder_awareness": 90,
                    "long_term_thinking": 95,
                    "ethical_consistency": 98,
                    "risk_awareness": 85
                },
                "consequence": {
                    "immediate_effect": "Dhritarashtra is pierced to the bone: 'Everything you say is true, Vidura, yet my heart clings to Duryodhana.'",
                    "secondary_consequence": "The king cannot plead ignorance before history; Vidura's words strip the regime of every rationalization.",
                    "stakeholder_impact": {
                        "Vidura": "Emerges as the towering ethical compass of the epic.",
                        "History": "Gains the timeless ethical treatise of Vidura Nīti.",
                        "The Assembly": "The moral benchmark is etched beyond dispute."
                    },
                    "strategic_impact": "Even if the king fails to act, the advisor has performed his ultimate duty without compromise.",
                    "ethical_tradeoff": "Accepts that truth must be spoken even when the recipient is likely too weak to change.",
                    "long_term_risk": "Personal marginalization by corrupt courtiers.",
                    "unintended_consequence": "Vidura survives the war with immaculate honor, counseling Yudhishthira in the reconstruction."
                }
            },
            {
                "id": "C",
                "title": "Ultimatum and Dramatic Resignation",
                "description": "Demand that Dhritarashtra arrest Duryodhana right now, or Vidura will resign his office that very night and depart into the forest.",
                "core_rationale": "Forcing immediate constitutional crisis through an all-or-nothing ultimatum.",
                "advantages": ["Makes an unmistakable public protest."],
                "risks": [
                    "Removes Vidura from the court prematurely; Shakuni takes over complete unchallenged control.",
                    "Leaves Kunti and the citizens with zero advocate in the capital."
                ],
                "reasoning_dimensions": {
                    "responsibility": 60,
                    "strategic_thinking": 45,
                    "stakeholder_awareness": 55,
                    "long_term_thinking": 48,
                    "ethical_consistency": 75,
                    "risk_awareness": 50
                },
                "consequence": {
                    "immediate_effect": "Dhritarashtra panics, but Duryodhana eagerly accepts the resignation.",
                    "secondary_consequence": "Shakuni takes over governance completely; moderate voices are expelled within 24 hours.",
                    "stakeholder_impact": {
                        "Court": "Total monopoly of extremists.",
                        "Vidura": "Safe in the forest, but unable to protect vulnerable palace residents."
                    },
                    "strategic_impact": "Premature forfeiture of advisory leverage.",
                    "ethical_tradeoff": "Purchased personal clean hands at the cost of abandoning vulnerable dependents.",
                    "long_term_risk": "Acceleration of catastrophe.",
                    "unintended_consequence": "The regime becomes more brutal without any internal friction."
                }
            },
            {
                "id": "D",
                "title": "Machiavellian Manipulation: Play on the King's Superstition and Fear",
                "description": "Invent astrological portents and ghostly omens predicting Dhritarashtra's personal gruesome death unless he yields to the Pandavas.",
                "core_rationale": "Using superstitious fear to achieve an ethical outcome when rational arguments fail.",
                "advantages": ["May temporarily terrify a superstitious king into concessions."],
                "risks": [
                    "Degrades governance to trickery and fraud.",
                    "Easily debunked by court astrologers on Duryodhana's payroll.",
                    "Destroys Vidura's credibility if uncovered."
                ],
                "reasoning_dimensions": {
                    "responsibility": 45,
                    "strategic_thinking": 60,
                    "stakeholder_awareness": 50,
                    "long_term_thinking": 35,
                    "ethical_consistency": 30,
                    "risk_awareness": 48
                },
                "consequence": {
                    "immediate_effect": "The king is frightened for a few hours until Shakuni brings rival priests to dispel the omens.",
                    "secondary_consequence": "Vidura is discredited as an alarmist peddler of superstitions.",
                    "stakeholder_impact": {
                        "Integrity": "Severe collapse of trust in the advisor."
                    },
                    "strategic_impact": "Short-term trickery fails against entrenched structural interest.",
                    "ethical_tradeoff": "Compromised truthfulness for opportunistic manipulation.",
                    "long_term_risk": "Permanent loss of advisory authority.",
                    "unintended_consequence": "Hardens the king's resolve against future genuine warnings."
                }
            }
        ],
        "principles": [
            {
                "id": "vidura-niti-counsel",
                "name": "The Unflinching Duty of the Ethical Advisor",
                "sanskrit_term": "विदुर नीति (Mahābhārata V.33–40)",
                "definition": (
                    "Vidura declares: 'He who speaks words that are pleasant to hear is easy to find, O King. "
                    "Rare indeed is the speaker and the listener of words that are unpalatable but wholesome (Apriyasya ca pathyasya vakta shrota ca durlabhah).' "
                    "The fiduciary duty of an advisor is to deliver diagnosis, not comforting delusion."
                ),
                "episode_connection": (
                    "Vidura refused to play the sycophant. He methodically mapped out how unconstrained attachment (Moha) "
                    "and willful blindness to institutional corruption inevitably culminate in systemic ruin."
                ),
                "modern_application": (
                    "Chief Risk Officers, compliance attorneys, and board directors must speak difficult operational truths to domineering founders "
                    "rather than enabling governance rot to safeguard stock options."
                ),
                "key_insight": "True loyalty to an institution often requires opposing the delusions of its current leader."
            }
        ],
        "modern_scenario": {
            "id": "modern-vidura-safety-report",
            "title": "The Building Inspection and the Manager's Shortcut",
            "domain": "Workplace Honesty & Speaking Truth to Authority",
            "context": (
                "You are an assistant site engineer at a construction firm. On Friday evening before Monday's public opening of a community school hall, "
                "you review the structural drainage load logs and discover an overlooked calculation error signed off by your senior project manager months ago. "
                "Under heavy rain, the roof joists could sag and crack. When you show the error to your manager privately, he is exhausted and defensive: "
                "'Do not report this now. It's a low probability risk, and halting Monday's opening will cost our firm the contract and get us both fired. "
                "We will quietly reinforce it during the winter holidays.'"
            ),
            "dilemma": (
                "Do you stay silent to protect your manager's career and avoid being labeled a troublemaker, or do you insist on reporting the flaw before children use the building?"
            ),
            "parallel_to_epic": (
                "Like Vidura counseling King Dhritarashtra in the quiet of the night, you are face to face with a leader blinded by anxiety and personal attachment, "
                "begging you to validate a dangerous shortcut. Speaking up carries real personal cost; staying silent makes you an accomplice."
            ),
            "options": [
                {
                    "id": "A",
                    "title": "Agree to Stay Silent and Hope for Winter Repairs",
                    "description": "Accept the manager's reassurance and sign off on the handover certificate.",
                    "primary_tradeoff": "Preserves your job and professional relationship today, but gambles with the safety of hundreds of people.",
                    "consequence_preview": "If rain damages the roof, you face direct liability and lifelong guilt for hiding a known danger."
                },
                {
                    "id": "B",
                    "title": "Insist on Transparent Disclosure (The Vidura Stand)",
                    "description": "Explain calmly to your manager that while delaying the opening is painful, compromising structural safety is impossible. Insist on a formal notification to the chief engineer for an emergency inspection over the weekend.",
                    "primary_tradeoff": "Triggers immediate workplace tension and delayed ceremonies, but prevents potential tragedy and upholds professional integrity.",
                    "consequence_preview": "The opening is modestly postponed for weekend bracing; lives are protected and your technical honesty is vindicated."
                },
                {
                    "id": "C",
                    "title": "Leak the Error Anonymously to the Local Press",
                    "description": "Send an anonymous email to the town newspaper on Friday night without confronting the engineering team.",
                    "primary_tradeoff": "Halts the opening, but creates public panic and burns your entire team without offering a chance to fix the calculation.",
                    "consequence_preview": "Creates a public scandal and internal witch-hunt."
                },
                {
                    "id": "D",
                    "title": "Quietly Resign without Stating Why",
                    "description": "Submit your resignation on Friday and walk away to protect yourself.",
                    "primary_tradeoff": "Protects your clean hands while allowing innocent people to walk into a hazardous building unalerted.",
                    "consequence_preview": "A total moral abdication that fails the primary obligation of a builder."
                }
            ]
        },
        "sources": [
            {
                "text": "The Mahābhārata: Udyogaparvan",
                "parva": "Udyoga Parva",
                "chapter_section": "BORI Critical Edition, Vol. 6, Chapters 33–40 (Prajāgara Parva / Vidura Nīti)",
                "critical_edition_ref": "BORI CE V.33.1 – V.40.30",
                "scholar_translation": "M.N. Dutt (1896) / P. Lal (Writers Workshop, 1968)",
                "scholarly_note": "Vidura Nīti represents a foundational text of Indian political philosophy (Nītiśāstra), emphasizing that unrighteous power inevitably collapses from internal moral rot.",
                "archive_link": "https://www.gitasupersite.iitk.ac.in"
            }
        ]
    },
    {
        "id": "karna-loyalty",
        "title": "Karna's Choice: Loyalty to a Patron vs Cosmic Justice",
        "subtitle": "Gratitude, Social Identity, and Conflicting Obligations",
        "parva": "Udyoga Parva",
        "chapter_reference": "Mahābhārata V.140–V.146 / Bhagavat Yāna Parva",
        "characters": ["Karna", "Krishna", "Duryodhana", "Kunti"],
        "category": "Loyalty vs Justice",
        "strategic_themes": ["Moral Obligations of Gratitude", "Identity and Stigma", "Tragic Ethical Conflict", "Personal Debt vs Public Good"],
        "ethical_themes": ["Mitra-Dharma (Loyalty to a Friend)", "Satya (Truth)", "Krita-Jnata (Gratitude)", "Tragic Heroism"],
        "difficulty": "Advanced",
        "estimated_time": "14-16 min",
        "order_index": 5,
        "context": (
            "During the failed peace mission, Krishna takes Karna on a solitary chariot ride outside the city walls. "
            "Krishna reveals the explosive secret of Karna's birth: he is not the son of a humble charioteer (Suta), "
            "but the eldest son of Kunti and the Sun God Surya. By sacred law, Karna is the rightful firstborn Pandava! "
            "Krishna promises that if Karna switches sides, the Pandavas will joyfully bow at his feet, Yudhishthira will hold his umbrella, "
            "Draupadi will accept him, and he will be anointed Emperor of all Bharatavarsha. The war would end instantly without a drop of blood. "
            "Yet for his entire youth, when the Pandavas and society mocked and humiliated him for his low caste status, "
            "only one man stood by him, crowned him King of Anga, and gave him honor and friendship: Duryodhana."
        ),
        "dilemma": (
            "Should Karna embrace cosmic truth, end the war, and claim the supreme imperial crown alongside his true brothers? "
            "Or should he honor his unbreakable personal loyalty and gratitude to Duryodhana, even knowing that Duryodhana is on the side of Adharma "
            "and that fighting with him will end in Karna's certain death and tragedy?"
        ),
        "why_difficult": (
            "This is one of world literature's most heartbreaking moral dilemmas. On one hand, joining the Pandavas stops a catastrophic war, "
            "aligns with objective cosmic justice, and claims his rightful heritage. On the other hand, abandoning Duryodhana on the eve of battle "
            "would be the ultimate betrayal of the one friend who gave him dignity when the world spat on him. "
            "Is gratitude to a personal benefactor higher than abstract duty to cosmic order?"
        ),
        "stakeholders": [
            {
                "name": "Karna (Radheya)",
                "role": "Champion Warrior & King of Anga",
                "interests": "Maintaining honor, keeping faith with gratitude, overcoming the stigma of low birth.",
                "risks": "Certain death on Kurukshetra; fighting his own younger brothers.",
                "expectations": "To be recognized as a hero whose word is more durable than gold.",
                "icon_name": "sun"
            },
            {
                "name": "Duryodhana",
                "role": "His Patron and Dearest Friend",
                "interests": "Relying on Karna's unmatched archery to defeat Arjuna.",
                "risks": "Complete emotional and military devastation if Karna abandons him.",
                "expectations": "Believes Karna is the one person on earth who will never desert him.",
                "icon_name": "shield"
            },
            {
                "name": "Kunti & The Pandavas",
                "role": "His Biological Mother and Estranged Brothers",
                "interests": "Reuniting their family, avoiding fratricide, gaining an invincible elder brother.",
                "risks": "Slaying their own brother in ignorance on the battlefield.",
                "expectations": "Hope that blood ties and imperial destiny will triumph over factional loyalty.",
                "icon_name": "heart"
            }
        ],
        "competing_values": [
            {
                "name": "Kritajnata & Mitra-Dharma (Gratitude and Loyalty to a Friend)",
                "sanskrit_term": "कृतज्ञता / मित्रधर्म",
                "description": "Unwavering loyalty to the person who stood by you in your hour of humiliation.",
                "polarity": "Personal Gratitude vs Universal Justice",
                "initial_weight": 95
            },
            {
                "name": "Samanya Dharma (Universal Righteousness & Peace)",
                "sanskrit_term": "सामान्य धर्म",
                "description": "Aligning with the cosmic and societal good to prevent widespread slaughter.",
                "polarity": "Public Good vs Private Debt",
                "initial_weight": 80
            },
            {
                "name": "Satya & Kula (Truth and Filial Belonging)",
                "sanskrit_term": "सत्य / कुल",
                "description": "Accepting one's true biological identity and reconciling with family.",
                "polarity": "Biological Kinship vs Chosen Alliance",
                "initial_weight": 60
            }
        ],
        "known_information": [
            "Karna is factually the firstborn son of Kunti and the legal heir to the Kuru throne.",
            "Duryodhana's entire war confidence rests upon Karna's promise to face Arjuna.",
            "Krishna Himself assures Karna that switching sides will avert the war and crown him emperor."
        ],
        "uncertain_information": [
            "Whether the Pandava brothers (especially Bhima and Arjuna) could genuinely accept his leadership without lingering resentment.",
            "Whether his conscience could ever survive the shame of abandoning Duryodhana at the hour of supreme danger."
        ],
        "assumptions": [
            "Karna knows that fighting for Duryodhana will result in his death: 'Where Krishna is, there is righteousness; where righteousness is, there is victory.'"
        ],
        "options": [
            {
                "id": "A",
                "title": "Accept Krishna's Offer: Claim the Crown and Unify the Dynasty",
                "description": "Publicly announce his birthright as Kunti's eldest son. Step into the Pandava chariot, stop the war, and assume the unified throne of Aryavarta.",
                "core_rationale": "Prevents the massacre of millions and aligns with cosmic justice over personal sentiment.",
                "advantages": [
                    "Averts the Kurukshetra war completely, saving hundreds of thousands of lives.",
                    "Restores Karna to his legitimate royal identity and supreme honor.",
                    "Reunites Kunti's shattered family."
                ],
                "risks": [
                    "Branded by history as a traitor who took 13 years of royal favors from Duryodhana only to jump ship for a crown.",
                    "Destroys Duryodhana psychologically and politically.",
                    "Deep internal guilt over abandoning the friend who gave him everything."
                ],
                "reasoning_dimensions": {
                    "responsibility": 82,
                    "strategic_thinking": 85,
                    "stakeholder_awareness": 88,
                    "long_term_thinking": 90,
                    "ethical_consistency": 65,
                    "risk_awareness": 80
                },
                "consequence": {
                    "immediate_effect": "Duryodhana is shattered; his war machine collapses without firing an arrow.",
                    "secondary_consequence": "The Pandavas crown Karna Emperor; peace is declared across the realm.",
                    "stakeholder_impact": {
                        "Civilization": "Saved from apocalyptic bloodbath.",
                        "Duryodhana": "Retreats into bitter solitude or suicide.",
                        "Karna": "Rules as a great monarch, but haunted forever by the ghost of his betrayed friend."
                    },
                    "strategic_impact": "Complete bloodless victory for systemic justice.",
                    "ethical_tradeoff": "Sacrifices personal honor and fidelity to a benefactor for the collective welfare of civilization.",
                    "long_term_risk": "The psychological agony of being viewed as a turncoat.",
                    "unintended_consequence": "Proves that utilitarian calculation triumphed over sacred personal gratitude."
                }
            },
            {
                "id": "B",
                "title": "Stay with Duryodhana with Tragic Integrity (The Historic Karna Stance)",
                "description": (
                    "Thank Krishna with deep tears for the revelation. Declare: 'Duryodhana fed me when I had no bread; he honored me when I had no name. "
                    "For thirteen years I have eaten his salt. To abandon him now when war has arrived would be the act of a dog. "
                    "I must fight on his side and die if necessary. But I promise this to Kunti: your five sons will still survive—either Arjuna or I will fall, but Kunti will always have five sons.'"
                ),
                "core_rationale": "Transcendent personal loyalty (Mitra-Dharma) and gratitude (Kritajnata) above personal life and imperial power.",
                "advantages": [
                    "Preserves sublime personal honor: refuses to be bought by an empire.",
                    "Demonstrates eternal loyalty to the friend who gave him dignity.",
                    "Concedes the safety of four brothers to his newly discovered mother."
                ],
                "risks": [
                    "Condemns himself and Duryodhana to certain death.",
                    "Allows the catastrophic war to proceed.",
                    "Dies fighting on the side of Adharma."
                ],
                "reasoning_dimensions": {
                    "responsibility": 70,
                    "strategic_thinking": 55,
                    "stakeholder_awareness": 75,
                    "long_term_thinking": 60,
                    "ethical_consistency": 88,
                    "risk_awareness": 65
                },
                "consequence": {
                    "immediate_effect": "Krishna embraces Karna with profound awe, acknowledging his peerless nobility of character.",
                    "secondary_consequence": "Karna enters the battle with tragic heroism, fighting fiercely yet withholding lethal strikes against Yudhishthira, Bhima, Nakula, and Sahadeva.",
                    "stakeholder_impact": {
                        "Duryodhana": "Has a loyal brother-in-arms till the very end.",
                        "Kunti": "Weeps over her fallen eldest son at the war's conclusion.",
                        "Arjuna": "Learns with horror after slaying Karna that he killed his own noble elder brother."
                    },
                    "strategic_impact": "Secures eternal immortal renown for tragic fidelity, though on the losing side.",
                    "ethical_tradeoff": "Chosen personal fidelity to a flawed benefactor over abstract universal justice.",
                    "long_term_risk": "Terminal tragedy for himself and his patron.",
                    "unintended_consequence": "Yudhishthira is so broken upon discovering Karna's identity that he nearly renounces the won kingdom in grief."
                }
            },
            {
                "id": "C",
                "title": "Confront Duryodhana with the Secret and Demand Peace Under Threat of Withdrawal",
                "description": "Tell Duryodhana the secret immediately: explain that the Pandavas are his own brothers, and demand that Duryodhana agree to Krishna's five-village peace proposal, warning that otherwise Karna will lay down his arms.",
                "core_rationale": "Using his immense leverage over Duryodhana to force a diplomatic resolution without betrayal.",
                "advantages": [
                    "Does not betray Duryodhana behind his back.",
                    "Leverages his indispensability to force the Kauravas into peace."
                ],
                "risks": [
                    "Duryodhana may feel betrayed that even Karna has been seduced by Krishna.",
                    "May trigger Duryodhana's paranoia, causing an ugly public rupture."
                ],
                "reasoning_dimensions": {
                    "responsibility": 78,
                    "strategic_thinking": 72,
                    "stakeholder_awareness": 80,
                    "long_term_thinking": 75,
                    "ethical_consistency": 76,
                    "risk_awareness": 70
                },
                "consequence": {
                    "immediate_effect": "Duryodhana is stunned into silence, sobbing that fate has stolen his final pillar of hope.",
                    "secondary_consequence": "Shakuni attempts to manipulate the situation, claiming the secret is a Pandava black-magic trick.",
                    "stakeholder_impact": {
                        "Duryodhana": "Faces the undeniable reality that his war cannot be won.",
                        "Karna": "Attempts to preserve both loyalty and peace."
                    },
                    "strategic_impact": "Maximum diplomatic pressure exerted from within the inner sanctum.",
                    "ethical_tradeoff": "Risks hurting his benefactor emotionally to save his life physically.",
                    "long_term_risk": "Uncertain whether Duryodhana's stubborness can be bent even by his dearest friend.",
                    "unintended_consequence": "Duryodhana may choose suicidal battle even alone."
                }
            },
            {
                "id": "D",
                "title": "Withdraw Completely from the Conflict to Anga",
                "description": "Declare that as the son of Surya and brother of both factions, he cannot fight on either side. Pack his chariot and return to his kingdom of Anga, remaining neutral.",
                "core_rationale": "Escaping the fratricidal curse while refusing to actively assist in the destruction of either party.",
                "advantages": ["Avoids killing brothers; avoids fighting against Krishna."],
                "risks": [
                    "Deserts Duryodhana at the exact moment he is most needed.",
                    "Both camps view him as someone who walked away when duty called."
                ],
                "reasoning_dimensions": {
                    "responsibility": 45,
                    "strategic_thinking": 40,
                    "stakeholder_awareness": 50,
                    "long_term_thinking": 45,
                    "ethical_consistency": 52,
                    "risk_awareness": 50
                },
                "consequence": {
                    "immediate_effect": "Duryodhana feels totally betrayed; Pandavas consider him an erratic outcast.",
                    "secondary_consequence": "The war proceeds anyway; Duryodhana is crushed quickly without Karna's archery.",
                    "stakeholder_impact": {
                        "Karna": "Survives physically, but ruined in public and personal self-respect."
                    },
                    "strategic_impact": "Passive abdication of a central historical actor.",
                    "ethical_tradeoff": "Chose personal neutrality over committed ethical engagement.",
                    "long_term_risk": "Lifelong exile and regret.",
                    "unintended_consequence": "The tragedy of the war is not reduced; only his moral stature is diminished."
                }
            }
        ],
        "principles": [
            {
                "id": "mitra-dharma-vs-samanya-dharma",
                "name": "Mitra-Dharma vs. Sāmānya-Dharma (The Tragedy of Competing Loyalties)",
                "sanskrit_term": "मित्रधर्म वि. सामान्यधर्म",
                "definition": (
                    "Karna embodies the profound Indian philosophical recognition that duties frequently collide irreconcilably. "
                    "Mitra-Dharma (the duty of gratitude and fidelity to a personal benefactor) is a real, sacred virtue; yet when attached "
                    "to a cause of Adharma, it tragically pits a noble soul against the cosmic order."
                ),
                "episode_connection": (
                    "Krishna did not condemn Karna as wicked; He recognized Karna's grandeur while pointing out the tragic flaw: "
                    "loyalty to an unrighteous patron inevitably implicates the loyal servant in the patron's catastrophic karma."
                ),
                "modern_application": (
                    "In professional life, a mentor or boss may have hired you when you were broke and defended you from detractors. "
                    "When that mentor later engages in fraud or harassment, you are torn between sacred gratitude and public ethics."
                ),
                "key_insight": "Gratitude to a human benefactor cannot absolve complicity in systemic injustice."
            }
        ],
        "modern_scenario": {
            "id": "modern-karna-mentor-debt",
            "title": "The Mentor's Unethical Demand",
            "domain": "Gratitude vs. Honesty in the Workplace",
            "context": (
                "Three years ago, when you were struggling to find work after graduation, a senior colleague took a personal chance on you, "
                "trained you patiently, and fought for your promotion. You owe your entire professional footing to their kindness. "
                "Today, during an internal project review, you discover this mentor has been systematically claiming billable credit for work completed "
                "by an unpaid summer intern and billing client accounts dishonestly. An internal auditor approaches you privately and asks whether "
                "the work logged under the mentor's name was actually completed by them."
            ),
            "dilemma": (
                "Do you lie or mislead the auditor to protect the person who gave you your start in life, or do you speak truthfully to protect the vulnerable intern?"
            ),
            "parallel_to_epic": (
                "Like Karna torn between his deep gratitude to Duryodhana (Mitra-Dharma) and the universal demands of righteousness (Sāmānya-Dharma), "
                "you are caught between a sacred personal debt to a benefactor and an undeniable injustice committed against someone weaker."
            ),
            "options": [
                {
                    "id": "A",
                    "title": "Falsify Records to Protect Your Mentor",
                    "description": "Tell the auditor that you personally witnessed the mentor doing the work, shielding them completely out of gratitude.",
                    "primary_tradeoff": "Demonstrates absolute personal loyalty, but participates in fraud and denies the intern fair credit and pay.",
                    "consequence_preview": "If discovered, your own career is destroyed for perjury; you become an accomplice to exploitation."
                },
                {
                    "id": "B",
                    "title": "Speak the Truth Impartially to the Auditor",
                    "description": "Answer the auditor's questions accurately and factually, stating who completed the work.",
                    "primary_tradeoff": "Upholds fairness for the intern and institutional honesty, but will be seen by your mentor as an unbearable betrayal.",
                    "consequence_preview": "Protects the intern and restores fairness, though you carry the heavy personal sorrow of your mentor's disappointment."
                },
                {
                    "id": "C",
                    "title": "Confront Your Mentor Privately Before Answering",
                    "description": "Go directly to your mentor. Tell them with deep gratitude for what they have done for you that you cannot lie to an auditor, and urge them to rectify the intern's credit themselves.",
                    "primary_tradeoff": "Offers the mentor a final chance to take moral ownership, though risking an angry, emotional confrontation.",
                    "consequence_preview": "Honors the relationship by being honest face to face, rather than speaking behind their back."
                },
                {
                    "id": "D",
                    "title": "Pretend You Don't Know and Evade the Question",
                    "description": "Tell the auditor you were too busy with your own tasks to notice who did what.",
                    "primary_tradeoff": "Tries to escape taking a stand, leaving the intern without an advocate while delaying the truth.",
                    "consequence_preview": "An evasion that satisfies neither gratitude nor justice."
                }
            ]
        },
        "sources": [
            {
                "text": "The Mahābhārata: Udyogaparvan",
                "parva": "Udyoga Parva",
                "chapter_section": "BORI Critical Edition, Vol. 6, Chapters 140–146 (Karna-Kṛṣṇa Saṁvāda)",
                "critical_edition_ref": "BORI CE V.140.1 – V.146.18",
                "scholar_translation": "J.A.B. van Buitenen (Univ. of Chicago Press, 1978) / K.M. Ganguli",
                "scholarly_note": "Karna's refusal of the throne is celebrated as one of the most sublime tragic soliloquies in ancient literature, illustrating that personal virtue (gratitude) detached from holistic Dharma leads to inevitable catastrophe.",
                "archive_link": "https://www.sacred-texts.com/hin/m05/index.htm"
            }
        ]
    },
    {
        "id": "abhimanyu-chakravyuha",
        "title": "Abhimanyu and the Chakravyuha",
        "subtitle": "Asymmetric Risk, Incomplete Knowledge, and Overextension under Pressure",
        "parva": "Drona Parva",
        "chapter_reference": "Mahābhārata VII.34–VII.49 / Abhimanyu-Vadha Parva",
        "characters": ["Abhimanyu", "Yudhishthira", "Drona", "Duryodhana", "Jayadratha"],
        "category": "Strategy & Risk Under Uncertainty",
        "strategic_themes": ["Knowledge Asymmetry", "Rollback Planning", "Team Interdependence", "Strategic Overextension"],
        "ethical_themes": ["Vira-Dharma (Courage)", "Leadership Accountability", "Fair Rules of Engagement", "Sacrifice vs Recklessness"],
        "difficulty": "Advanced",
        "estimated_time": "12-15 min",
        "order_index": 6,
        "context": (
            "On the thirteenth day of the Kurukshetra war, preceptor Drona arranges the Kaurava forces into the impenetrable, rotating "
            "labyrinthine formation known as the Chakravyuha (Wheel Phalanx). Arjuna has been deliberately lured far away to the southern horizon "
            "by the Samsaptaka suicide warriors. The Chakravyuha advances relentlessly, threatening to annihilate the entire Pandava host before sunset. "
            "Only four people in the world know how to penetrate the Chakravyuha: Krishna, Arjuna, Pradyumna, and sixteen-year-old Abhimanyu. "
            "However, Abhimanyu possesses a fatal limitation: he overheard the secret of piercing INTO the formation while in his mother Subhadra's womb, "
            "but his mother fell asleep before Arjuna could explain the secret of how to FIGHT ONE'S WAY OUT. "
            "In desperate panic, King Yudhishthira pleads with the adolescent warrior: 'Break the barrier, my child! We will follow directly in your wake, "
            "protecting your flanks and rear with our four divisions.'"
        ),
        "dilemma": (
            "Does Abhimanyu accept an asymmetric, one-way operational mission knowing he has no autonomous exit capability, "
            "trusting his older teammates to support him under chaotic conditions? "
            "And how should Yudhishthira evaluate the catastrophic risk of deploying a half-informed youth into an irreversible labyrinth?"
        ),
        "why_difficult": (
            "If Abhimanyu refuses, the Pandava army faces imminent collapse on day 13, and the allied kings will be routed. "
            "If he attacks, he depends 100% on a fragile operational assumption: that Yudhishthira and Bhima can breach the entrance behind him. "
            "When King Jayadratha seals the breach using a divine boon, Abhimanyu is trapped inside the hostile core, "
            "facing six veteran Maharathas who violate the chivalric code to encircle and slay him."
        ),
        "stakeholders": [
            {
                "name": "Abhimanyu (The Youthful Champion)",
                "role": "Sixteen-Year-Old Hero",
                "interests": "Defending his family, demonstrating peerless valor, stopping the army's collapse.",
                "risks": "Trapped without exit strategy; death by multi-directional encirclement.",
                "expectations": "Counts on his uncles to breach the wall behind him as promised.",
                "icon_name": "target"
            },
            {
                "name": "Yudhishthira & The Pandava High Command",
                "role": "The Leaders Under Existential Crisis",
                "interests": "Halting Drona's unstoppable Chakravyuha before the army breaks.",
                "risks": "Sacrificing their beloved nephew and facing Arjuna's unbearable grief.",
                "expectations": "Hope that raw courage and unified momentum can compensate for lack of exit knowledge.",
                "icon_name": "shield"
            },
            {
                "name": "Drona & The Kaurava Command",
                "role": "The Master Tacticians",
                "interests": "Exploiting Arjuna's absence to crush the Pandava army in a single day.",
                "risks": "Severe reputational disgrace if chivalric rules are violated.",
                "expectations": "To capture Yudhishthira and force a surrender.",
                "icon_name": "compass"
            }
        ],
        "competing_values": [
            {
                "name": "Yukti (Prudent Strategic Risk Management)",
                "sanskrit_term": "युक्ति",
                "description": "Never committing operational assets into an irreversible environment without verified rollback capability.",
                "polarity": "Prudent Strategy vs Desperate Heroism",
                "initial_weight": 80
            },
            {
                "name": "Kshatra-Tejas (Heroic Valor and Courage under Duress)",
                "sanskrit_term": "क्षात्रतेजस्",
                "description": "The sacred warrior mandate to step into the breach when all others falter.",
                "polarity": "Courage vs Calculated Caution",
                "initial_weight": 85
            },
            {
                "name": "Sangha-Vishvasa (Team Trust and Dependency)",
                "sanskrit_term": "संघविश्वास",
                "description": "Relying on allied promises to maintain flank support during high-risk execution.",
                "polarity": "Distributed Dependency vs Self-Reliant Security",
                "initial_weight": 70
            }
        ],
        "known_information": [
            "Abhimanyu knows with certainty how to breach the outer perimeter of the Chakravyuha.",
            "He explicitly tells Yudhishthira: 'I know how to enter, but my father never taught me how to emerge.'",
            "Drona's formation is slaughtering hundreds of Pandava soldiers per hour."
        ],
        "uncertain_information": [
            "Whether the Kauravas possess a hidden tactical asset (such as Jayadratha's Shiva-boon) capable of holding the rear breach.",
            "Whether the Kaurava commanders will adhere to single-combat chivalric rules once surrounded."
        ],
        "assumptions": [
            "Yudhishthira assumes that Bhima and Satyaki's brute force can overpower any Kaurava rear-guard and keep the gate open."
        ],
        "options": [
            {
                "id": "A",
                "title": "Refuse the One-Way Mission: Order a Disciplined Tactical Retreat",
                "description": "Abhimanyu explicitly declines: 'I cannot enter an irreversible trap without an exit pathway.' Yudhishthira sounds the conch for an organized defensive retreat to defensive trenches until Arjuna returns at sunset.",
                "core_rationale": "Strict adherence to operational safety and refusal to deploy assets with asymmetric exit vulnerability.",
                "advantages": [
                    "Saves Abhimanyu's life and prevents the devastating loss of the next-generation leader.",
                    "Preserves Pandava combat cohesion without gambling on unverified dependencies."
                ],
                "risks": [
                    "Heavy casualties among rear-guard soldiers during the retreat.",
                    "Loss of battlefield territory and temporary drop in allied morale."
                ],
                "reasoning_dimensions": {
                    "responsibility": 84,
                    "strategic_thinking": 92,
                    "stakeholder_awareness": 82,
                    "long_term_thinking": 90,
                    "ethical_consistency": 85,
                    "risk_awareness": 94
                },
                "consequence": {
                    "immediate_effect": "Pandava forces fall back in disciplined order under cover of arrow barrages.",
                    "secondary_consequence": "Drona captures ground, but the sun sets without the capture of Yudhishthira.",
                    "stakeholder_impact": {
                        "Abhimanyu": "Survives to fight another day alongside his father.",
                        "Arjuna": "Returns at twilight to find his son and brothers alive and ready to plan a counter-offensive.",
                        "Pandava Army": "Absorbs tactical losses, but avoids catastrophic strategic decapitation."
                    },
                    "strategic_impact": "Classic defense-in-depth: sacrificed space for time, preserving critical assets.",
                    "ethical_tradeoff": "Accepted minor battlefield humiliation to avert fatal overextension.",
                    "long_term_risk": "Short-term morale hit, fully remediated by Arjuna's return.",
                    "unintended_consequence": "Drona is frustrated that his trap caught no grand prize."
                }
            },
            {
                "id": "B",
                "title": "Solo Penetration with Trust in Unverified Support (The Historic Episode)",
                "description": (
                    "Driven by peerless courage and devotion to his uncles, Abhimanyu charges the wheel phalanx alone, smashing through Drona's front lines. "
                    "However, Jayadratha seals the breach behind him. Cut off from all reinforcement, Abhimanyu wreaks havoc inside until encircled "
                    "by six veteran Maharathas who disarm him from behind and strike him down."
                ),
                "core_rationale": "Supreme heroic sacrifice and unhesitating commitment to the family's survival.",
                "advantages": [
                    "Saves the Pandava army from being routed on day 13.",
                    "Exposes the moral bankruptcy of the Kaurava commanders who violate the Kshatriya code of single combat.",
                    "Immortalizes Abhimanyu as the ultimate archetype of youthful valor."
                ],
                "risks": [
                    "Guaranteed death if the single point of failure (the rear door) is blocked.",
                    "Devastates Arjuna with grief and rage upon his return.",
                    "Losing the heir of the entire Pandava dynasty."
                ],
                "reasoning_dimensions": {
                    "responsibility": 68,
                    "strategic_thinking": 48,
                    "stakeholder_awareness": 65,
                    "long_term_thinking": 40,
                    "ethical_consistency": 78,
                    "risk_awareness": 42
                },
                "consequence": {
                    "immediate_effect": "Abhimanyu's chariot cuts a blazing swath through the Kaurava ranks, slaying Duryodhana's son Lakshmana.",
                    "secondary_consequence": "Jayadratha repulses Bhima and Yudhishthira at the bottleneck; Abhimanyu is completely isolated inside.",
                    "stakeholder_impact": {
                        "Abhimanyu": "Fights with breathtaking glory using a chariot wheel when disarmed, before falling surrounded.",
                        "Yudhishthira": "Plunged into inconsolable guilt and grief.",
                        "Kauravas": "Their victory is tainted forever as a shameful, cowardly gang murder."
                    },
                    "strategic_impact": "Tactical breach achieved at the unacceptable cost of the primary future asset.",
                    "ethical_tradeoff": "Relied on wishful thinking regarding allied support in a zero-margin environment.",
                    "long_term_risk": "Pushes the war into total ruthlessness, stripping away all remaining chivalric rules.",
                    "unintended_consequence": "Arjuna swears a terrible oath to slay Jayadratha before sunset the next day or enter a funeral pyre, escalating stakes to the brink of catastrophe."
                }
            },
            {
                "id": "C",
                "title": "Synchronized Dual Penetration: Advance Only if Bhima and Satyaki Are Locked at His Side",
                "description": "Refuse to dart ahead as a solo scout. Form a three-chariot wedge with Bhima on the left and Satyaki on the right, matching speed so the entrance is physically widened and held open as they enter.",
                "core_rationale": "Converting a fragile single-point-of-failure charge into an integrated multi-unit breach.",
                "advantages": [
                    "Prevents Jayadratha from isolating Abhimanyu.",
                    "Combines Abhimanyu's navigation knowledge with Bhima's brute force to anchor the breach."
                ],
                "risks": [
                    "Slows down Abhimanyu's initial velocity; Drona has more time to reinforce the opening.",
                    "Still carries high risk inside the labyrinth."
                ],
                "reasoning_dimensions": {
                    "responsibility": 88,
                    "strategic_thinking": 85,
                    "stakeholder_awareness": 84,
                    "long_term_thinking": 80,
                    "ethical_consistency": 82,
                    "risk_awareness": 82
                },
                "consequence": {
                    "immediate_effect": "The Pandava wedge hits the perimeter with massive coordinated impact, cracking the rotating ring.",
                    "secondary_consequence": "Jayadratha cannot close the gap because Bhima's massive mace anchors the rear.",
                    "stakeholder_impact": {
                        "Pandava Command": "Maintains continuous two-way communication and reinforcement lines.",
                        "Abhimanyu": "Supported by veteran warriors inside the phalanx."
                    },
                    "strategic_impact": "High operational discipline prevents isolation and catastrophic loss.",
                    "ethical_tradeoff": "Disciplined coordination over impulsive individual glory.",
                    "long_term_risk": "High casualty rate, but shared across the command rather than concentrated on a single youth.",
                    "unintended_consequence": "Neutralizes Drona's strategic trap without losing the next generation."
                }
            },
            {
                "id": "D",
                "title": "Send Envoys to Recall Arjuna Immediately While Stalling Drona",
                "description": "Send fast camel-riders to alert Arjuna of the deception. In the meantime, deploy sacrificial defensive illusions (Ghatotkacha's Rakshasa army) to stall the Chakravyuha's advance.",
                "core_rationale": "Matching the correct asset (Arjuna) to the problem rather than throwing an unprepared asset into the fire.",
                "advantages": ["Protects Abhimanyu and calls back the only master capable of dismantling the formation."],
                "risks": ["Takes hours; Drona may break through intermediate defenses before Arjuna returns."],
                "reasoning_dimensions": {
                    "responsibility": 80,
                    "strategic_thinking": 82,
                    "stakeholder_awareness": 78,
                    "long_term_thinking": 82,
                    "ethical_consistency": 80,
                    "risk_awareness": 80
                },
                "consequence": {
                    "immediate_effect": "Ghatotkacha creates night illusions that disorient the Kauravas; messengers gallop south.",
                    "secondary_consequence": "Arjuna disengages from the Samsaptakas and turns his chariot back toward the main camp.",
                    "stakeholder_impact": {
                        "Pandavas": "Hold the line with heavy attrition, but no leadership decapitation."
                    },
                    "strategic_impact": "Defensive containment until primary counter-measures arrive.",
                    "ethical_tradeoff": "Accepted asset wear-and-tear to avoid reckless tactical gambling.",
                    "long_term_risk": "Close timing margin.",
                    "unintended_consequence": "Demonstrates mature crisis escalation management."
                }
            }
        ],
        "principles": [
            {
                "id": "yukti-and-prati-vyuha",
                "name": "Yukti (Prudent Strategic Architecture and Rollback Safeguards)",
                "sanskrit_term": "युक्ति वि. साहस (Strategy vs Recklessness)",
                "definition": (
                    "In classical Indian warfare treatises (Arthaśāstra and Mahābhārata), true bravery (Vīrya) is never synonymous with recklessness (Sāhasa). "
                    "Deploying human capital into an operation with an ingress plan but no tested egress/rollback mechanism "
                    "violates the foundational stewardship duty of leadership."
                ),
                "episode_connection": (
                    "Yudhishthira's agonizing confession after the war reflects this eternal principle: in his desperation to survive the day, "
                    "he placed an unfair, fatal burden upon a brilliant junior who possessed only half the necessary operational blueprint."
                ),
                "modern_application": (
                    "In software engineering, high-stakes infrastructure deployments, or venture expansion, never deploy irreversible "
                    "database migrations or enter high-risk markets without a tested, end-to-end rollback and containment plan."
                ),
                "key_insight": "Never deploy an asset into a labyrinth where ingress is known but egress is an assumption."
            }
        ],
        "modern_scenario": {
            "id": "modern-abhimanyu-unverified-pitch",
            "title": "The Decisive Pitch without Verified Backup",
            "domain": "Responsibility, Incomplete Information & Peer Dependency",
            "context": (
                "You are a dedicated junior associate at a non-profit foundation. On the morning of a vital community grant presentation "
                "that could fund your organization for the entire year, the senior director suddenly falls ill. The team lead turns to you: "
                "'You understand the community outreach portion well! Step into the panel room alone and lead the pitch. The rest of the team will join "
                "by conference phone to answer the complex financial and legal questions.' You know how to introduce the mission, but you have no experience "
                "defending the budget projections, and committee rooms frequently forbid remote conference phones due to confidentiality rules."
            ),
            "dilemma": (
                "Do you accept an irreversible solo responsibility on the assumption of unverified remote backup, or do you request a formal rescheduling?"
            ),
            "parallel_to_epic": (
                "Like Abhimanyu entering the Chakravyuha knowing how to breach the perimeter but lacking knowledge of how to exit and depending "
                "entirely on promised support behind him, you are asked to step into a high-stakes environment with only half the necessary operational blueprint."
            ),
            "options": [
                {
                    "id": "A",
                    "title": "Step In Alone on Pure Bravery",
                    "description": "Enter the panel room alone, hoping the phone connection works and bluffing through any financial queries.",
                    "primary_tradeoff": "Heroic effort under pressure, but catastrophic vulnerability if the panel asks detailed financial questions that you cannot answer.",
                    "consequence_preview": "The phone connection is disallowed; you are grilled on legal liabilities and the grant is rejected."
                },
                {
                    "id": "B",
                    "title": "Request a Short, Formal Rescheduling",
                    "description": "Politely inform the grant committee chair of the director's sudden illness and formally request a 48-hour reschedule with the full team present.",
                    "primary_tradeoff": "May cause minor initial irritation, but ensures the organization presents a fully verified, competent proposal.",
                    "consequence_preview": "The panel respects the professionalism of not presenting half-baked answers; the full team pitches successfully two days later."
                },
                {
                    "id": "C",
                    "title": "Enter with Limited Scope and Clear Ground Rules",
                    "description": "Agree to present only the community outreach section, explicitly informing the panel up front that the financial review must be conducted in writing or in a second session.",
                    "primary_tradeoff": "Manages expectations transparently, though testing the panel's patience for a phased pitch.",
                    "consequence_preview": "Highlights your core strengths without risking catastrophic overextension on unfamiliar data."
                },
                {
                    "id": "D",
                    "title": "Refuse and Walk Away",
                    "description": "Refuse the assignment abruptly and let the slot lapse completely.",
                    "primary_tradeoff": "Avoids personal failure, but causes the organization to forfeit the grant without trying.",
                    "consequence_preview": "Severely damages your professional standing and funding for community programs."
                }
            ]
        },
        "sources": [
            {
                "text": "The Mahābhārata: Droṇaparvan",
                "parva": "Drona Parva",
                "chapter_section": "BORI Critical Edition, Vol. 8, Chapters 34–49 (Abhimanyu-vadha Parva)",
                "critical_edition_ref": "BORI CE VII.34.1 – VII.49.28",
                "scholar_translation": "Kisari Mohan Ganguli (1888) / J.A.B. van Buitenen & Bibek Debroy (Penguin, 2012)",
                "scholarly_note": "The death of Abhimanyu marks the tragic turning point of the epic, where the unyielding adherence to strategic deception and the abandonment of chivalric rules of war (Dharma-yuddha) begin to accelerate.",
                "archive_link": "https://www.sacred-texts.com/hin/m07/index.htm"
            }
        ]
    }
]
