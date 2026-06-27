import argparse
import sys


ROLE_LABELS = {
    "pm": "PM",
    "supervisor": "监督",
    "long-worker": "长工",
    "short-worker": "短工",
    "acceptance": "验收",
}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Render a starter prompt pack for the PM orchestration skill."
    )
    parser.add_argument(
        "--role",
        required=True,
        choices=sorted(ROLE_LABELS.keys()),
        help="Operating role for the new thread.",
    )
    parser.add_argument("--module", required=True, help="Owned module or lane name.")
    parser.add_argument("--version", required=True, help="Human-readable module version.")
    parser.add_argument(
        "--mode",
        default="goal",
        choices=["goal", "dispatch", "review", "standby"],
        help="Primary execution mode.",
    )
    parser.add_argument(
        "--modules",
        default="core",
        help="Comma-separated optional modules, for example git,archive,validation.",
    )
    parser.add_argument(
        "--truth-source",
        default="docs/orchestration/index.md",
        help="Primary truth-source file or board path.",
    )
    return parser


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    args = build_parser().parse_args()
    role = ROLE_LABELS[args.role]
    module_list = [item.strip() for item in args.modules.split(",") if item.strip()]
    module_text = ", ".join(module_list) if module_list else "core"

    print(f"[{role}]#{args.module}@{args.version}")
    print()
    print(f"Mode: {args.mode}")
    print(f"Active optional modules: {module_text}")
    print(f"Truth source: {args.truth_source}")
    print()
    print("Execution rules:")
    print("1. Read the truth source first.")
    print("2. Keep one active goal.")
    print("3. Default to summary-package delivery, not full git diff.")
    print("4. Do not expand scope.")
    print("5. Write back completed, incomplete, blockers, and next action.")
    print()
    if args.role == "long-worker":
        print("Role note: own one large module only; split child lanes into short-workers when needed.")
    elif args.role == "short-worker":
        print("Role note: day-close only; do not continue across days without archive and re-open.")
    elif args.role == "pm":
        print("Role note: dispatch, acceptance, correction, and close-out only.")
    elif args.role == "supervisor":
        print("Role note: inspect PM drift and issue the smallest correction.")
    elif args.role == "acceptance":
        print("Role note: verify behavior, evidence, and rollback surface.")


if __name__ == "__main__":
    main()
