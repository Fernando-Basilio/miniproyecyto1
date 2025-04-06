  
import cv2
import mediapipe as mp

# Inicializar MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

# Captura de video
cap = cv2.VideoCapture(0)

# Variables para el objeto
object_position = (300, 300)
object_size = 50
is_dragging = False

def is_grabbing(hand_landmarks):
    # Obtener las posiciones de los dedos índice y pulgar
    thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
    index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]

    # Calcular la distancia entre el pulgar y el índice
    distance = ((thumb_tip.x - index_tip.x) ** 2 + (thumb_tip.y - index_tip.y) ** 2) ** 0.5
    return distance < 0.05  # Ajusta este umbral según sea necesario

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            if is_grabbing(hand_landmarks):
                is_dragging = True
                # Obtener la posición de los dedos índice y pulgar
                thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
                index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]

                # Calcular la posición media entre el pulgar y el índice
                hand_x = int((thumb_tip.x + index_tip.x) / 2 * frame.shape[1])
                hand_y = int((thumb_tip.y + index_tip.y) / 2 * frame.shape[0])
                object_position = (hand_x, hand_y)
            else:
                is_dragging = False

    # Dibujar el objeto
    if is_dragging:
        cv2.circle(frame, object_position, object_size, (0, 255, 0), -1)  # Color verde
    else:
        cv2.circle(frame, object_position, object_size, (0, 0, 255), -1)  # Color rojo

    cv2.imshow("Drag and Drop", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
