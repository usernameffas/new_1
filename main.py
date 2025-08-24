#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
미션 컴퓨터 로그 분석기 (기본 버전)
화성 기지 사고 원인 파악을 위한 로그 파일 분석 프로그램
"""


def print_hello_mars():
    """테스트용 Hello Mars 출력 함수"""
    print('Hello Mars')
    print('미션 컴퓨터 로그 분석을 시작합니다...')
    print()


def read_log_file(filename):
    """
    로그 파일을 읽어서 내용을 반환하는 함수
    
    Args:
        filename (str): 읽을 로그 파일명
    
    Returns:
        list: 로그 파일의 각 라인을 담은 리스트 또는 None
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        print(f'{filename} 파일을 성공적으로 읽었습니다.')
        print(f'총 {len(lines)}줄의 로그 데이터가 있습니다.')
        print()
        
        return lines
    
    except FileNotFoundError:
        print(f'오류: {filename} 파일을 찾을 수 없습니다.')
        return None
    except PermissionError:
        print(f'오류: {filename} 파일에 대한 읽기 권한이 없습니다.')
        return None
    except Exception as e:
        print(f'예상치 못한 오류가 발생했습니다: {e}')
        return None


def display_logs(log_lines):
    """
    로그를 화면에 출력하는 함수
    
    Args:
        log_lines (list): 로그 라인들
    """
    print('=== 미션 컴퓨터 로그 내용 ===')
    print()
    
    for i, line in enumerate(log_lines, 1):
        line = line.strip()
        if line:  # 빈 줄이 아닌 경우만 출력
            print(f'{i:3d}: {line}')
    
    print()
    print(f'총 {len([l for l in log_lines if l.strip()])}줄의 유효한 로그가 있습니다.')


def main():
    """메인 함수"""
    # Hello Mars 출력
    print_hello_mars()
    
    # 로그 파일명
    log_filename = 'mission_computer_main.log'
    
    # 로그 파일 읽기
    log_lines = read_log_file(log_filename)
    
    if log_lines is None:
        print('로그 파일을 읽을 수 없습니다. 프로그램을 종료합니다.')
        return
    
    # 로그 내용 화면에 출력
    display_logs(log_lines)
    
    print()
    print('미션 컴퓨터 로그 분석이 완료되었습니다.')


if __name__ == '__main__':
    main()
