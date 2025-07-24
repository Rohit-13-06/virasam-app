from utils.ai_fallback import get_ai_response, get_fast_ai_response, get_comprehensive_ai_response, get_smart_ai_response
import time

test_questions = [
    "What is folk culture?",  # Simple question
    "Explain the historical origins and cultural significance of traditional folk dances in rural communities",  # Complex question
    "Tell me about traditional recipes"  # Medium question
]

print("=== Testing Dual Model Support ===\n")

for i, question in enumerate(test_questions, 1):
    print(f"Question {i}: {question}")
    print("-" * 60)
    
    # Test Fast Model
    print("🚀 Fast Model (llama3.2:1b):")
    start_time = time.time()
    fast_response = get_fast_ai_response(question)
    fast_time = time.time() - start_time
    print(f"Response: {fast_response}")
    print(f"Time: {fast_time:.2f} seconds")
    print()
    
    # Test Smart Model (auto-selection)
    print("🧠 Smart Model (auto-select):")
    start_time = time.time()
    smart_response = get_smart_ai_response(question)
    smart_time = time.time() - start_time
    print(f"Response: {smart_response}")
    print(f"Time: {smart_time:.2f} seconds")
    print()
    
    # Optional: Test Comprehensive Model (only if you want to wait)
    # print("🎯 Comprehensive Model (llama3:latest):")
    # start_time = time.time()
    # comprehensive_response = get_comprehensive_ai_response(question)
    # comprehensive_time = time.time() - start_time
    # print(f"Response: {comprehensive_response}")
    # print(f"Time: {comprehensive_time:.2f} seconds")
    
    print("=" * 80)
    print()
