import os
from openai import OpenAI
from dotenv import load_dotenv
from llm.prompts.prompts import build_prompt_planner, build_prompt_generator, build_prompt_hook, build_prompt_validator, build_prompt_fixer

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def plan_video(idea, theme):

    prompt = build_prompt_planner(idea, theme)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
    {"role": "system", "content": "You are an expert film director..."},
    {"role": "user", "content": prompt}
        ],
        response_format={"type": "json_object"}
    )

    return response.choices[0].message.content

def plan_hook(idea, theme, first_scene_arc):

    prompt = build_prompt_hook(idea, theme, first_scene_arc)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
    {"role": "system", "content": "You are an expert film director..."},
    {"role": "user", "content": prompt}
        ],
        response_format={"type": "json_object"}
    )

    return response.choices[0].message.content

def generate_content(idea, theme, hook, number_of_scenes, scene_arcs, target_duration, style):
        
    prompt = build_prompt_generator(idea, theme, hook, number_of_scenes, scene_arcs, target_duration, style)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
    {"role": "system", "content": "You are an expert film director and storyboard artist..."},
    {"role": "user", "content": prompt}
        ],
        response_format={"type": "json_object"}
    )

    return response.choices[0].message.content

def validate_content(hook, number_of_scenes, scene_arcs, generator_response):
    
    prompt = build_prompt_validator(hook, number_of_scenes, scene_arcs, generator_response)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
    {"role": "system", "content": "You are an expert film director and storyboard artist..."},
    {"role": "user", "content": prompt}
        ],
        response_format={"type": "json_object"}
    )

    return response.choices[0].message.content

def fix_content(generator_response, validator_errors, validator_score):
    
    prompt, regen_signal = build_prompt_fixer(generator_response, validator_errors, validator_score)

    if regen_signal:
        return regen_signal
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
    {"role": "system", "content": "You are an expert film director and storyboard artist..."},
    {"role": "user", "content": prompt}
        ],
        response_format={"type": "json_object"}
    )

    return response.choices[0].message.content